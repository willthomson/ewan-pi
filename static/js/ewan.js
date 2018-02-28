new Vue({
  el: '#ewan',
  data: {},
  methods: {
    ewanOn: function () {
      console.log("on");
      fetch('/on');
    },
    ewanOff: function () {
      fetch('/off');
    },
    ewanRepeat: function () {
      fetch('/repeat');
    },
  }
});
