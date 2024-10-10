document.addEventListener("DOMContentLoaded", function() {
    fetch('/manhwa')
        .then(response => response.json())
        .then(data => {
            const manhwaList = document.getElementById('manhwa-list');
            data.forEach(manhwa => {
                const manhwaCard = `
                    <div class="manhwa-card">
                        <img src="${manhwa.image_url}" alt="${manhwa.title}">
                        <div class="manhwa-title">${manhwa.title}</div>
                        <div class="manhwa-genre">${manhwa.genre}</div>
                        <div class="manhwa-Writer">${manhwa.Writer}</div>
                        <div class="manhwa-Art">${manhwa.Art}</div>
                        <div class="manhwa-Reads">${manhwa.Reads}</div>
                        <div class="manhwa-description">${manhwa.description}</div>
                    </div>
                `;
                manhwaList.innerHTML += manhwaCard;
            });
        });
});
