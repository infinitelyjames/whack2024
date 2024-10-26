

using System;

public class EventDetails {
    private string title;
    private string description;
    private float probability;
    private Action onEventTriggered;
    
    public EventDetails(string title, string description, float probability, Action onEventTriggered) {
        this.title = title;
        this.description = description;
        this.probability = probability;
        this.onEventTriggered = onEventTriggered;
    }

}