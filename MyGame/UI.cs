using System;
using System.Collections;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

public abstract class Sprite {
    public Texture2D texture;
    public Vector2 Position {get; set;}
    public float Rotation {get; set;}

    public Sprite(Texture2D _texture, Vector2 _position, float _rotation){
        this.texture = _texture;
        Position = _position;
        Rotation = _rotation;
    }

    public abstract void Update(GameTime gameTime);

    public abstract void Draw(GameTime gameTime, SpriteBatch spriteBatch);
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