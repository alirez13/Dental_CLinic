(function($){
	"use strict";
	jQuery(document).on('ready', function () {

        // Header Sticky
		$(window).on('scroll',function() {
            if ($(this).scrollTop() > 120){  
                $('.navbar-area').addClass("is-sticky");
            }
            else{
                $('.navbar-area').removeClass("is-sticky");
            }
        });

        // Mean Menu
		jQuery('.mean-menu').meanmenu({
			meanScreenWidth: "991"
        });

        // Search Popup JS
        $('.others-option .close-btn').on('click',function() {
            $('.search-overlay').fadeOut();
            $('.search-btn').show();
            $('.close-btn').removeClass('active');
        });
        $('.others-option .search-btn').on('click',function() {
            $(this).hide();
            $('.search-overlay').fadeIn();
            $('.close-btn').addClass('active');
        });

        // Sidebar Modal
        $(".burger-menu").on('click',  function() {
			$('.sidebar-modal').toggleClass('active');
		});
        $(".sidebar-modal-close-btn").on('click',  function() {
			$('.sidebar-modal').removeClass('active');
        });

        // Home Slides
		$('.home-slides').owlCarousel({
			loop: true,
			nav: true,
            dots: false,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            items: 1,
            animateOut: 'fadeOut',
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ]
        });
        $(".home-slides").on("translate.owl.carousel", function(){
            $(".main-banner-content .sub-title").removeClass("animated fadeInLeft").css("opacity", "0");
            $(".main-banner-content h1").removeClass("animated fadeInLeft").css("opacity", "0");
            $(".main-banner-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content .btn-box .btn").removeClass("animated fadeIn").css("opacity", "0");
            $(".main-banner-content .btn-box .video-btn").removeClass("animated fadeIn").css("opacity", "0");
        });
        $(".home-slides").on("translated.owl.carousel", function(){
            $(".main-banner-content .sub-title").addClass("animated fadeInLeft").css("opacity", "1");
            $(".main-banner-content h1").addClass("animated fadeInLeft").css("opacity", "1");
            $(".main-banner-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content .btn-box .btn").addClass("animated fadeIn").css("opacity", "1");
            $(".main-banner-content .btn-box .video-btn").addClass("animated fadeIn").css("opacity", "1");
        });

		// Why Choose Us Image Slides
		$('.why-choose-us-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: true,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            items: 1,
            animateOut: 'fadeOut',
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ]
        });

        // Popup Video
		$('.popup-youtube').magnificPopup({
			disableOn: 320,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
        });
		
		// Odometer JS
        $('.odometer').appear(function(e) {
			var odo = $(".odometer");
			odo.each(function() {
				var countNumber = $(this).attr("data-count");
				$(this).html(countNumber);
			});
        });
        
        // FAQ Accordion
        $(function() {
            $('.accordion').find('.accordion-title').on('click', function(){
                // Adds Active Class
                $(this).toggleClass('active');
                // Expand or Collapse This Panel
                $(this).next().slideToggle('fast');
                // Hide The Other Panels
                $('.accordion-content').not($(this).next()).slideUp('fast');
                // Removes Active Class From Other Titles
                $('.accordion-title').not($(this)).removeClass('active');		
            });
        });
		
		// Doctor Slides
		$('.doctor-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            margin: 30,
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ],
			responsive: {
                0: {
                    items: 1,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 3,
                },
                1200: {
                    items: 4,
				}
            }
        });

        // Feedback Slides
		$('.feedback-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            items: 1,
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ]
        });

        // Nice Select JS
        $('select').niceSelect();

        // Partner Slides
		$('.partner-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            margin: 30,
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ],
			responsive: {
                0: {
                    items: 2,
                },
                576: {
                    items: 3,
                },
                768: {
                    items: 3,
                },
                1200: {
                    items: 5,
				}
            }
        });

        // Services Details Image Slides
		$('.services-details-image-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: true,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            items: 1,
            animateOut: 'fadeOut',
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ]
        });

        // Research Details Image Slides
		$('.research-details-image-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: true,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: false,
            items: 1,
            animateOut: 'fadeOut',
            navText: [
                "<i class='flaticon-back'></i>",
                "<i class='flaticon-next-1'></i>"
            ]
        });

        // Feedback Carousel
		var $imagesSlider = $(".testimonial-slides .client-feedback>div"),
		$thumbnailsSlider = $(".client-thumbnails>div");
		// Images Options
		$imagesSlider.slick({
			speed: 300,
			slidesToShow: 1,
			slidesToScroll: 1,
			cssEase: 'linear',
			fade: true,
            rtl: true,
			autoplay: false,
			draggable: true,
			asNavFor: ".client-thumbnails>div",
			prevArrow: '.client-feedback .prev-arrow',
			nextArrow: '.client-feedback .next-arrow'
		});
		// Thumbnails Options
		$thumbnailsSlider.slick({
			speed: 300,
			slidesToShow: 5,
			slidesToScroll: 1,
			cssEase: 'linear',
			autoplay: false,
            rtl: true,
			centerMode: true,
			draggable: false,
			focusOnSelect: true,
			asNavFor: ".testimonial-slides .client-feedback>div",
			prevArrow: '.client-thumbnails .prev-arrow',
            nextArrow: '.client-thumbnails .next-arrow',
        });

        // Subscribe form
		$(".newsletter-form").validator().on("submit", function (event) {
			if (event.isDefaultPrevented()) {
			// handle the invalid form...
				formErrorSub();
				submitMSGSub(false, "لطفا ایمیل خود را به درستی وارد کنید.");
			} else {
				// everything looks good!
				event.preventDefault();
			}
		});
		function callbackFunction (resp) {
			if (resp.result === "success") {
				formSuccessSub();
			}
			else {
				formErrorSub();
			}
		}
		function formSuccessSub(){
			$(".newsletter-form")[0].reset();
			submitMSGSub(true, "با تشکر ثبت شد!");
			setTimeout(function() {
				$("#validator-newsletter").addClass('hide');
			}, 4000)
		}
		function formErrorSub(){
			$(".newsletter-form").addClass("animated shake");
			setTimeout(function() {
				$(".newsletter-form").removeClass("animated shake");
			}, 1000)
		}
		function submitMSGSub(valid, msg){
			if(valid){
				var msgClasses = "validation-success";
			} else {
				var msgClasses = "validation-danger";
			}
			$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
		}
		// AJAX MailChimp
		$(".newsletter-form").ajaxChimp({
			url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
			callback: callbackFunction
        });

        // Go to Top
        $(function(){
            // Scroll Event
            $(window).on('scroll', function(){
                var scrolled = $(window).scrollTop();
                if (scrolled > 600) $('.go-top').addClass('active');
                if (scrolled < 600) $('.go-top').removeClass('active');
            });  
            // Click Event
            $('.go-top').on('click', function() {
                $("html, body").animate({ scrollTop: "0" },  500);
            });
        });

        // TwentyTwenty JS
        $(function(){
            $(".twentytwenty-container[data-orientation!='vertical']").twentytwenty({default_offset_pct: 0.5});
        });
        
    });

    // WOW JS
	$(window).on ('load', function (){
        if ($(".wow").length) { 
            var wow = new WOW({
            boxClass:     'wow',      // Animated element css class (default is wow)
            animateClass: 'animated', // Animation css class (default is animated)
            offset:       20,         // Distance to the element when triggering the animation (default is 0)
            mobile:       true,       // Trigger animations on mobile devices (default is true)
            live:         true,       // Act on asynchronously loaded content (default is true)
          });
          wow.init();
        }
    });
    
    // Preloader
	jQuery(window).on('load', function() {
		$('.preloader').fadeOut();
	});
}(jQuery));