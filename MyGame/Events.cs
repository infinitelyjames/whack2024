

using System;
using System.Collections.Generic;

public class Event {
    private string title;
    private string description;
    private float probability;
    private Action onEventTriggered;
    
    public Event(string title, string description, float probability, Action onEventTriggered) {
        this.title = title;
        this.description = description;
        this.probability = probability;
        this.onEventTriggered = onEventTriggered;
    }

    public void Trigger() {
        onEventTriggered();
    }

    public void RandomTrigger() {
        Random random = new Random();
        if (random.NextDouble() < probability) {
            Trigger();
        }
    }
}

public class EventController {
    private List<Event> events = new List<Event>();

    public EventController(List<Event> events) {
        this.events = events;
    }

    public void TriggerRandomEvents() {
        foreach (Event e in events) {
            e.RandomTrigger();
        }
    }
}