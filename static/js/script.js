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
  $('#summernote').summernote({
    styleTags: [
      'p', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
    ],
    toolbar: [
      // [groupName, [list of button]]
      ['style', ['bold', 'italic', 'underline', 'clear', 'pre']],
      ['font', ['strikethrough', 'superscript', 'subscript']],
      ['fontsize', ['fontsize']],
      ['color', ['color']],
      ['para', ['ul', 'ol', 'paragraph']],
      ['insert', ['picture', 'link', 'video']],
      ['help', ['help']],
      ['style', ['style']],
    ]
  });
});