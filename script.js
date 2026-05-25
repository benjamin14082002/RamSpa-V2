document.addEventListener("DOMContentLoaded", () => {
    // --- LÓGICA DEL MENÚ ---
    const navbar = document.querySelector(".navbar");
    const menuBtn = document.getElementById("mobile-menu-btn");
    const navLinks = document.getElementById("nav-links");
    const links = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = "0 4px 15px rgba(0,0,0,0.1)";
        } else {
            navbar.style.boxShadow = "0 2px 10px rgba(0,0,0,0.05)";
        }
    });

    menuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    links.forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("active");
        });
    });

    // --- CONFIGURACIÓN DEL CARRUSEL (SWIPER) ---
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,      // Cuántas fotos se ven por defecto (móvil)
        spaceBetween: 20,      // Espacio entre fotos
        loop: true,            // Carrusel infinito
        grabCursor: true,      // Cambia el cursor a "manito"
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        // Responsividad del Carrusel
        breakpoints: {
            640: {
                slidesPerView: 2, // En tablets muestra 2 fotos
                spaceBetween: 20,
            },
            1024: {
                slidesPerView: 3, // En PC muestra 3 fotos
                spaceBetween: 30,
            },
        },
    });

    console.log("RAM SPA V2 cargado. Carrusel activo.");
});