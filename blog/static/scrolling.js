(function() {

    const nav_list = document.getElementById("nav-list");
    const li_list = nav_list.getElementsByTagName("LI");
    const content_box_list = document.querySelectorAll(".content-box");
    const scroll_events = ['load', 'scroll'];

    const scroll_to_top = document.getElementById("scroll-to-top");
    let scroll_position;

    for (let i = 0; i < scroll_events.length; i++) {
        window.addEventListener(scroll_events[i], function() {
            if (window.pageYOffset <= 0) {
                scroll_to_top.style.opacity = "0";
            }
            else if (window.pageYOffset > 0 && window.pageYOffset <= 200) {
                scroll_position = window.pageYOffset;
                scroll_to_top.style.opacity = scroll_position/200;
            }
            else if (window.pageYOffset > 200) {
                scroll_to_top.style.opacity = "1";
            }
        });
    }

    for (let i = 0; i < li_list.length; i++) {
        li_list[i].addEventListener('click', () => window.scrollTo({
            top: content_box_list[i].offsetTop,
            behavior: 'smooth'
        }));
    }

    scroll_to_top.addEventListener('click', () => window.scrollTo({
        top: 0,
        behavior: 'smooth'
    }));

})();