// simple interactive animation for mouse move on plan cards
document.addEventListener('mousemove', function(e){ document.querySelectorAll('.plan-card').forEach(function(card){
  const rX = (e.clientX - window.innerWidth/2) / 40;
  const rY = (e.clientY - window.innerHeight/2) / 40;
  card.style.transform = 'perspective(800px) rotateY('+rX+'deg) rotateX('+(-rY)+'deg)';
})});
