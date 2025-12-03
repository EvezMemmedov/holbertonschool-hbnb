document.addEventListener('DOMContentLoaded', () => {
    // Login səhifəsi
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            loginUser();
        });
    }

    // Price filter və places siyahısı səhifəsi
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', filterPlaces);
        checkAuthentication();
    }

    // Place details səhifəsi
    const placeDetails = document.getElementById('place-details');
    if (placeDetails) {
        loadPlaceDetails();
    }

    // Add review səhifəsi
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', submitReview);
    }
});

// Burada bütün funksiyalar (loginUser, checkAuthentication, filterPlaces, loadPlaceDetails, submitReview) 
// layihə tələblərinə uyğun şəkildə JS kod ilə yazılacaq
