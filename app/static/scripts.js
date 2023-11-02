// Function to add hover effect on list items
function addHoverEffect() {
    const listItems = document.querySelectorAll('ul#uf2-files-list li, ul#txt-files-list li');
    listItems.forEach((item) => {
        item.addEventListener('mouseover', () => {
            item.style.border = '2px solid white';
        });
        item.addEventListener('mouseout', () => {
            item.style.border = '2px dashed lime';
        });
    });
}

// Run functions when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    addHoverEffect();
});