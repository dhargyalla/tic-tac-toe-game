// includeHTML.js
document.addEventListener("DOMContentLoaded", function() {
    var includeElements = document.querySelectorAll('[data-include]');

    includeElements.forEach(function(el) {
        var file = el.getAttribute("data-include");
        fetch(file)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                el.innerHTML = data;
            })
            .catch(error => console.error('Error loading file:', error));
    });
});
