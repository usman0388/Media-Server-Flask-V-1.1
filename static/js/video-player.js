var player = videojs('videoPlayer',{
    autoplay: false,
    controls: true,
    
    fluid: true,
    // aspectRatio: '16:9',
    playbackRates: [0.25,0.5,1,1.5,2,2.5],
    userActions: {
        hotkeys: true
    }
});
// vjs-control-bar