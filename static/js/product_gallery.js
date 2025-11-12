/**
 * product gallery management
 */
function main(gallery) {
  // ===== Init main image & thumbs =====
  const stage = document.getElementById('zoomStage');
  const thumbs = document.getElementById('thumbs');

  const leftBtn = document.getElementById("thumbs_left_btn");
  const rightBtn = document.getElementById("thumbs_right_btn");


  // const leftBtn = document.getElementById("leftBtn");
  // const rightBtn = document.getElementById("rightBtn");


  function setStageImage(url) {
      stage.style.backgroundImage = `url('${url}')`;
      stage.classList.remove('zooming');
  }

  function selectImage(index) {
      const url = gallery[index];
      setStageImage(url);
      // highlight active thumb
      if (thumbs) {
          [...thumbs.children].forEach(el => el.classList.remove('active'));
          const active = thumbs.querySelector(`[data-index="${index}"]`);
          if (active) active.classList.add('active');
      }
      document.getElementById('active_image').setAttribute('data-active-image-id',
          (index).toString());
  }

  function scrollImageRight() {
      let active_thumb = document.getElementById('active_image');
      let active_image = parseInt(active_thumb.getAttribute('data-active-image-id'));
      console.log(gallery.length, active_image);

      if (active_image < gallery.length - 1){
          selectImage(active_image + 1);
          document.getElementById('active_image').setAttribute('data-active-image-id',
              (active_image + 1).toString());
      }
  }

    function scrollImageLeft() {
      let active_thumb = document.getElementById('active_image');
      let active_image = parseInt(active_thumb.getAttribute('data-active-image-id'));
      console.log(gallery.length, active_image);

      if (active_image > 0){
          selectImage(active_image - 1);
          document.getElementById('active_image').setAttribute('data-active-image-id',
              (active_image - 1).toString());
      }
  }


  // ===== Zoom behavior (click to toggle, move to pan) =====
  let zoomOn = false;

  function toggleZoom() {
      zoomOn = !zoomOn;
      stage.classList.toggle('zooming', zoomOn);
  }

  function panZoom(e) {
      if (!zoomOn) return;
      const rect = stage.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      stage.style.backgroundPosition = `${x}% ${y}%`;
  }

  rightBtn.addEventListener('click', () => {
      scrollImageRight();
  })
  leftBtn.addEventListener('click', () => {
      scrollImageLeft();
  })

  for (let i=1; i <= gallery.length;i++){
     document.getElementById(`img_${i}`).addEventListener('click', () => {
         selectImage(i-1);
     })
  }
    document.addEventListener('DOMContentLoaded', () => {
      selectImage(0);
  })

  stage.addEventListener('click', toggleZoom);
  stage.addEventListener('mousemove', panZoom);
  stage.addEventListener('mouseleave', () => {
      if (zoomOn) stage.style.backgroundPosition = 'center';
  });

} // EOF main

main(GALLERY);