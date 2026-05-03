/**
 * product gallery management
 */
function main(gallery) {
    const stage = document.getElementById('zoomStage');
    const thumbs = document.getElementById('thumbs');
    const leftBtn = document.getElementById("thumbs_left_btn");
    const rightBtn = document.getElementById("thumbs_right_btn");
    const activeImageTracker = document.getElementById('active_image');

    if (!stage || !gallery || gallery.length === 0) return;

    function setStageImage(url) {
        if (!url) return;
        stage.style.backgroundImage = `url('${url}')`;
        stage.classList.remove('zooming');
    }

    function selectImage(index) {
        if (index < 0 || index >= gallery.length) return;
        const url = gallery[index];
        setStageImage(url);
        
        if (thumbs) {
            [...thumbs.children].forEach(el => el.classList.remove('active'));
            const active = thumbs.querySelector(`[data-index="${index}"]`);
            if (active) active.classList.add('active');
        }
        
        if (activeImageTracker) {
            activeImageTracker.setAttribute('data-active-image-id', index.toString());
        }
    }

    function scrollImageRight() {
        if (!activeImageTracker) return;
        let active_image = parseInt(activeImageTracker.getAttribute('data-active-image-id') || "0");
        if (active_image < gallery.length - 1) {
            selectImage(active_image + 1);
        }
    }

    function scrollImageLeft() {
        if (!activeImageTracker) return;
        let active_image = parseInt(activeImageTracker.getAttribute('data-active-image-id') || "0");
        if (active_image > 0) {
            selectImage(active_image - 1);
        }
    }

    // Zoom behavior
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

    if (rightBtn) rightBtn.addEventListener('click', scrollImageRight);
    if (leftBtn) leftBtn.addEventListener('click', scrollImageLeft);

    for (let i = 1; i <= gallery.length; i++) {
        const thumbImg = document.getElementById(`img_${i}`);
        if (thumbImg) {
            thumbImg.addEventListener('click', () => selectImage(i - 1));
        }
    }

    selectImage(0);

    stage.addEventListener('click', toggleZoom);
    stage.addEventListener('mousemove', panZoom);
    stage.addEventListener('mouseleave', () => {
        if (zoomOn) stage.style.backgroundPosition = 'center';
    });
}

function initGallery() {
    const galleryDataElement = document.getElementById('gallery-data');
    if (galleryDataElement) {
        try {
            const gallery = JSON.parse(galleryDataElement.textContent);
            main(gallery);
        } catch (e) {
            console.error("Gallery data parse error:", e);
        }
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGallery);
} else {
    initGallery();
}
