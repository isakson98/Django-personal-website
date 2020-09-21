$.fn.stars = function() {
    return $(this).each(function() {
        const rating = $(this).data("rating");
        const numStars = $(this).data("numStars");
        const fullStar = '<i class="fas fa-star fa-sm"></i>'.repeat(Math.floor(rating));
        const noStar = '<i class="far fa-star fa-sm"></i>'.repeat(Math.floor(numStars-rating));
        $(this).html(`${fullStar}${noStar}`);
    });
}