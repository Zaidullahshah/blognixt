"use strict";
const blueRex = {
  status: 0,
  setParams: (data, url = "") => {
    let h = "";
    for (let k in data) h += k + "=" + data[k] + "&";
    if (h.substr(-1) === "&") h = h.substring(0, h.length - 1);
    if (url != "") {
      if (url.split("?").length > 1) {
        url = `${url}&${h}`;
      } else {
        url = `${url}?${h}`;
      }
      return url;
    } else {
      return h;
    }
  },
  get: (url, data = {}, headers = {}, async = true) => {
    let x = new XMLHttpRequest();
    blueRex.status = 0;
    return new Promise((a, b) => {
      x.onreadystatechange = function () {
        if (this.readyState === 4) {
          if (this.status === 200) {
            let t = this.response;
            a(t);
          } else {
            b(this.response);
          }
          blueRex.status = x.status;
        }
      };
      let url_ = blueRex.setParams(data, url);
      x.open("GET", url_, async);
      x.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      for (let header in headers) x.setRequestHeader(header, headers[header]);
      x.send(url_);
    });
  },
  post: (url, data = {}, headers = {}, async = true) => {
    blueRex.status = 0;
    let x = new XMLHttpRequest();
    return new Promise((a, b) => {
      x.onreadystatechange = function () {
        if (this.readyState === 4) {
          if (this.status === 200) {
            let t = this.response;
            a(t);
          } else {
            b(this.response);
          }
          blueRex.status = x.status;
        }
      };
      x.open("POST", url, async);
      x.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      for (let header in headers) x.setRequestHeader(header, headers[header]);
      x.send(blueRex.setParams(data));
    });
  },
};
