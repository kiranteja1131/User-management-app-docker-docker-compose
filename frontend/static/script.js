// Display a welcome message in the browser console
console.log("User Management Platform loaded successfully.");

// Add a small animation to dashboard cards
document.querySelectorAll(".stat-card").forEach((card, index) => {
    card.style.animation = `appear 0.5s ease ${index * 0.15}s both`;
});

// Confirm logout
document.querySelectorAll(".logout").forEach(link => {
    link.addEventListener("click", function(event) {
        if (!confirm("Are you sure you want to logout?")) {
            event.preventDefault();
        }
    });
});