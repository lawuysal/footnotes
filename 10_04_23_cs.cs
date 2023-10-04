using System;
using System.Threading;

// Events and Delegates

///
public class HelloWorld 
{
  static void Main() 
  {
    var myVideo = new Video() {Title = "Video 1"};
    var myVideoEncoder = new VideoEncoder();
    var myMailService = new MailService();
    var myMessageService = new MessageService();
    
    myVideoEncoder.videoEncoded += myMailService.onVideoEncoded;
    myVideoEncoder.videoEncoded += myMessageService.onVideoEncoded;
    
    myVideoEncoder.encode(myVideo);
  }
}

///
public class Video 
{
    public string Title { get; set; }
}

///
public class VideoEncoder 
{
    // 1- Define a delegate
    //public delegate void videoEncoderEventHandler (object source, VideoEventArgs args);
    
    // 2- Define a event based on that delegate
    public event EventHandler<VideoEventArgs> videoEncoded;
    
    // 3- Raise the event
    
    protected virtual void onVideoEncoded (Video _video)
    {
        if (videoEncoded != null)
        {
            videoEncoded( this, new VideoEventArgs() { video = _video } );
        }
    }
    
    
    
    public void encode (Video video)
    {
        Console.WriteLine("Video encoding....");
        Thread.Sleep(3000);
        
        // Raised the event
        onVideoEncoded(video);
    }
}

///
public class MailService 
{
    public void onVideoEncoded (object source, VideoEventArgs e)
    {
        Console.WriteLine("Sending: email..." + e.video.Title);
    }
}


///
public class MessageService
{
    public void onVideoEncoded (object source, VideoEventArgs e)
    {
        Console.WriteLine("MessageService: Sending message...." + e.video.Title);
    }
}

///
public class VideoEventArgs : EventArgs
{
    public Video video { get; set; }
}