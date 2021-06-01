// Using https://infinite-scroll.com/, under GPLv3, personal websites
// init Infinite Scroll
$('.container-infinite-scroll').infiniteScroll({
  path: '.next > a',
  append: '#infinite-scroll',
  status: '.scroller-status',
  hideNav: '.pagination',
});