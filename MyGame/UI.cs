using System;
using System.Collections;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

public abstract class Sprite {
    public Texture2D texture;
    public Vector2 Position {get; set;}
    public float Rotation {get; set;}

    public Sprite(Texture2D _texture, Vector2 _position, float _rotation){
        this.texture = _texture;
        Position = _position;
        Rotation = _rotation;
        EntityManager.AddSprite(this);
    }

    public abstract void Update(GameTime gameTime);

    public abstract void Draw(GameTime gameTime, SpriteBatch spriteBatch);
}

public class PieChart : Sprite {

    private GraphicsDevice graphicsDevice;
    public PieChart(Texture2D _texture, Vector2 _position): base(_texture, _position, 0){}

    // public Texture2D CreateCircle(int radius)
    // {
    //     int outerRadius = radius*2 + 2; // So circle doesn't go out of bounds
    //     Texture2D texture = new Texture2D(graphicsDevice, outerRadius, outerRadius);

    //     Color[] data = new Color[outerRadius * outerRadius];

    //     // Colour the entire texture transparent first.
    //     for (int i = 0; i < data.Length; i++)
    //         data[i] = Color.Transparent;

    //     // Work out the minimum step necessary using trigonometry + sine approximation.
    //     double angleStep = 1f/radius;

    //     for (double angle = 0; angle < Math.PI*2; angle += angleStep)
    //     {
    //         // Use the parametric definition of a circle: http://en.wikipedia.org/wiki/Circle#Cartesian_coordinates
    //         int x = (int)Math.Round(radius + radius * Math.Cos(angle));
    //         int y = (int)Math.Round(radius + radius * Math.Sin(angle));

    //         data[y * outerRadius + x + 1] = Color.White;
    //     }

    //     texture.SetData(data);
    //     return texture;
    // }
    

    public override void Update(GameTime gameTime){}

    public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
    {
        spriteBatch.Draw(texture, Position, null, Color.White);
    }
}

public class Button : Sprite {
    public int buttonX, buttonY;
    private MouseState oldState;
    private SpriteFont font;
    public Button(Texture2D _texture, Vector2 _position, SpriteFont _font): base(_texture, _position, 0){
        buttonX = (int)Position.X;
        buttonY = (int)Position.Y;
        font = _font;
    }

    public bool enterButton(MouseState mouseState){
        if (mouseState.X < buttonX + texture.Width &&
                    mouseState.X > buttonX &&
                    mouseState.Y < buttonY + texture.Height &&
                    mouseState.Y > buttonY)
            {
                return true;
            }
            return false;
    }

    public override void Update(GameTime gameTime)
    {
        MouseState newState = Mouse.GetState();

        if(enterButton(newState) && oldState.LeftButton == ButtonState.Released && newState.LeftButton == ButtonState.Pressed){
            Console.WriteLine("This Button Works");
        }

        oldState = newState;
    }

    public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
    {
        spriteBatch.Draw(texture, Position, null, Color.White);  
        spriteBatch.DrawString(font, "Button", new Vector2(Position.X+texture.Width/2, Position.Y+texture.Height/2), Color.Black);
    }
}

public static class EntityManager{
    public static List<Sprite> sprites = new List<Sprite>();

    public static void AddSprite(Sprite sprite){
        sprites.Add(sprite);
    }

    public static void RemoveSprite(Sprite sprite){
        sprites.Remove(sprite);
        sprite = null;
        GC.Collect();
        GC.WaitForPendingFinalizers();
    }


    public static void Update(GameTime gameTime){
        foreach(Sprite sprite in sprites){
            sprite.Update(gameTime);
        }
    }
    public static void Draw(GameTime gameTime, SpriteBatch spriteBatch){
        foreach(Sprite sprite in sprites){
            sprite.Draw(gameTime, spriteBatch);
        }
    }
}