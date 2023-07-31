const video = document.getElementById('myVideo');
video.autoplay = true
video.addEventListener('loadeddata', function() {
    video.loop = true;
    video.play();
});

video.addEventListener('play', function() {
  this.controls = false;
});
