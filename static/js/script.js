// // Using https://infinite-scroll.com/, under GPLv3, personal websites
// // init Infinite Scroll
$('.container-infinite-scroll').infiniteScroll({
  // options
  path: '.pagination > li:last-child > a', // selecting last list child, or pagination class, to target the next link
  append: '#infinite-scroll', // Add to container with id infinite-scroll
  hideNav: '.pagination', // hide pagination navigation links
  history: true,
});
// Help found with last child selector from https://api.jquery.com/last-child-selector/

// Summernote WYSIWYG editor, loading on page ready
$(document).ready(function() {
  $('#summernote').summernote();
});