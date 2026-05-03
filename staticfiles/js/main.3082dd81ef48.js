/**
 * Site-wide functions
 */

/**
 * Filter products by category on mobile
 * @param {string} categoryId - The ID of the category to filter by
 */
function filterMobileCategory(categoryId) {
    const sections = document.querySelectorAll('.category-section');
    sections.forEach(function (sec) {
        if (categoryId === 'all') {
            sec.style.display = 'block';
        } else {
            sec.style.display = (sec.id === categoryId) ? 'block' : 'none';
        }
    });
}
