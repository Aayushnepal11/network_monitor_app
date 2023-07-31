const navLinks = document.querySelectorAll('.nav-link');

function setActiveLink(event) {
  navLinks.forEach(link => {
    link.classList.remove('active');
  });

  const clickedLink = event.target;
  clickedLink.classList.add('active');
}

navLinks.forEach(link => {
  link.addEventListener('click', setActiveLink());
});
