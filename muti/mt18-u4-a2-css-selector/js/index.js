function changeSize(x){
  size = x.getAttribute('size');
  if(size == 's'){x.setAttribute('size','m');}
  if(size == 'm'){x.setAttribute('size','l');}
  if(size == 'l'){x.setAttribute('size','s');}
}