{
  function closeSearchModal() {
    document.querySelector(".search-result").style.display = "none";
  }
  let search_container = false;
  if (document.getElementById("search-container")) {
    search_container = document.querySelector(
      "#search-container .search-list-33839s"
    );
    counter_sec = document.querySelector(".search-count-322");
  }
  let timeOutFunc = false;
  function SearchItems(e) {
    if (e.value.length == 0)
      document.querySelector(".search-result").style.display = "none";
    else document.querySelector(".search-result").style.display = "block";
    if (timeOutFunc) clearTimeout(timeOutFunc);
    timeOutFunc = setTimeout(async () => {
      document.querySelector(
        "#search-container .search-list-33839s"
      ).innerHTML = ` <div class="search-loading l60 h20"></div>
      <div class="search-loading l20 h30"></div>
      <div class="search-loading l60 h20"></div>
      <div class="search-loading l40 h20"></div>`;
      await blueRex
        .get(`api/search/${e.value}`)
        .then((res) => {
          res = JSON.parse(res);
          counter_sec.innerHTML = res.items_length;
          if (res.items_length == 0) {
            search_container.innerHTML =
              "<h5>Not found check your search term!</h5>";
            return;
          }
          let html = "";
          res?.products?.length > 0
            ? (html = `
            <h5 class="search-title-xxd">Check these items</h5>
            <div class="blog-right">`)
            : "";
          res?.products?.map((item) => {
            html += `
            <a class="side-bar-item-links " href="/products/${
              item.slug
            }" title="view ${item.title}">
              <section class="df ac">
                  <div class="left-acc">
                      <img
                          src="${
                            item.image != ""
                              ? "/media/" + item.image
                              : item.image_link
                          }"
                          alt="${item.title.substr(0, 8)}"
                      />
                      </div>
                      <div class="uryal">
                      <h3>${
                        item.title.charAt(0).toUpperCase() + item.title.slice(1)
                      }</h3>
                      <div class="yellow-roar">
                          <span class="abc-dd3la2">
                            Price <i class="fa fa-usd"></i>${item.price}
                            ${
                              item.isNew
                                ? '<span class="new-badge side-bar-sec1224">New</span>'
                                : ""
                            }
                          </span>
                        </div>
                  </div>
              </section>
          </a>
          `;
          });
          res?.blogs?.length > 0
            ? (html += `
          </div>
          <h5 class="search-title-xxd">Blogs</h5>
          <div class="blog-right">`)
            : "";
          res?.blogs?.map((item) => {
            html += `
            <a class="side-bar-item-links " href="/blogs/${
              item.slug
            }" title="view ${item.title}">
              <section class="df ac">
                  <div class="left-acc">
                      <img
                          src="${
                            item.image != ""
                              ? "/media/" + item.image
                              : item.image_link
                          }"
                          alt="${item.title.substr(0, 8)}"
                      />
                      </div>
                      <div class="uryal">
                      <h3>${
                        item.title.charAt(0).toUpperCase() + item.title.slice(1)
                      }</h3>
                      <div class="yellow-roar">
                          <span class="abc-dd3la2" style="font-size:11px !important">
                          ${item.author} - ${new Date(
              item.createdAt
            ).getDate()}/${new Date(item.createdAt).getMonth()}/${new Date(
              item.createdAt
            ).getFullYear()}
                            ${
                              item.isNew
                                ? '<span class="new-badge side-bar-sec1224">New</span>'
                                : ""
                            }
                          </span>
                        </div>
                  </div>
              </section>
          </a>
          `;
          });
          res?.categories?.length > 0
            ? (html += `
          </div>
          <h5 class="search-title-xxd">Categories</h5>
          <div class="blog-right">`)
            : "";
          res?.categories?.map((item) => {
            html += `
            <a class="side-bar-item-links " href="/products/category/${
              item.slug
            }" title="view ${item.name}">
              <section class="df ac">
                  <h3>${
                    item.name.charAt(0).toUpperCase() + item.name.slice(1)
                  }</h3>
              </section>
          </a>
          `;
          });
          search_container.innerHTML = html;
        })
        .catch((e) => {
          console.error(e);
        });
    }, 800);
  }
}
class LoadTagsData {
  constructor() {
    this.container = document.querySelector("#load-tags-data");
    this.tags = document.querySelector("#tags-list").value;
    this.cur_id = document.querySelector("#cur_id").value;
    if (this.tags.length > 0) {
      this.getData(this.tags, this.cur_id);
    }
  }
  setUpHtml(data) {
    this.container.innerHTML = "";
    data?.tags_data?.map((item) => {
      let sec = `<section class="product-view-sec mlr-10">
              <span class="title">${
                item.title.charAt(0).toUpperCase() + item.title.slice(1)
              }</span>
              <div class="stars-cont product-list-view">
                <i
                  class="${
                    item.stars >= 1
                      ? "fa-solid fa-star"
                      : item.stars >= 0.5
                      ? "fa-solid fa-star-half-stroke"
                      : "fa fa-star-o"
                  }"
                  aria-hidden="true"
                ></i>
                <i
                  class="${
                    item.stars >= 2
                      ? "fa-solid fa-star"
                      : item.stars >= 1.5
                      ? "fa-solid fa-star-half-stroke"
                      : "fa fa-star-o"
                  }
                  aria-hidden="true"
                ></i>
                <i
                  class="${
                    item.stars >= 3
                      ? "fa-solid fa-star"
                      : item.stars >= 2.5
                      ? "fa-solid fa-star-half-stroke"
                      : "fa fa-star-o"
                  }
                  aria-hidden="true"
                ></i>
                <i
                  class="${
                    item.stars >= 4
                      ? "fa-solid fa-star"
                      : item.stars >= 3.5
                      ? "fa-solid fa-star-half-stroke"
                      : "fa fa-star-o"
                  }
                  aria-hidden="true"
                ></i>
                <i
                  class="${
                    item.stars >= 5
                      ? "fa-solid fa-star"
                      : item.stars >= 4.5
                      ? "fa-solid fa-star-half-stroke"
                      : "fa fa-star-o"
                  }
                  aria-hidden="true"
                ></i>
                <span class="ytll"> ${item.stars} </span>
              </div>
              <div>
              <img 
                id="product-list-view"
                src="${
                  item.image != "" ? "/media/" + item.image : item.image_link
                }"
                alt="${item.title}" /></div>
              <div class="ac93jk29">
                <span>Category ${item.category}</span>
                <span>Price <i class="fa fa-usd"></i>${item.price}</span>
              </div>
              <div class="df ac jc yellow-c">
                <a href="/products/${
                  item.slug
                }" class="side-bar-link mr-5" title="Buy (${
        item.title
      }) Product">View Details</a>
                <a href="/products/${
                  item.slug
                }" class="side-bar-link ml-5" title="Buy (${
        item.title
      }) Product">Buy Now <i class="fab fa-amazon"></i></a>
              </div>
            </section>
      `;
      this.container.innerHTML += sec;
    });
  }
  async getData(tags, cur_id) {
    await blueRex
      .get(`/api/get-tags-data/${tags}/${cur_id}`)
      .then((res) => {
        this.setUpHtml(JSON.parse(res));
      })
      .catch((e) => {
        console.error(e);
      });
  }
}
class IntersectingLazyLoading {
  constructor() {
    const images = Array.from(
      document.querySelectorAll(".load-lazy-not-yet img")
    );
    if ("IntersectionObserver" in window) {
      images.forEach((img) => this.InterSectImage().observe(img));
    } else {
      images.forEach((img) => {
        img.src = img.dataset.src;
        img.previousElementSibling.remove();
      });
    }
  }
  InterSectImage() {
    return new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const image = entry.target;
          let src = image.dataset.src;
          image.src = image.dataset.src;
          image.style.height = "";
          if (image.previousElementSibling)
            image.onload = () => image.previousElementSibling.remove();
          observer.unobserve(image);
        }
      });
    });
  }
}

class IntersectingStyles {
  constructor() {
    document.querySelectorAll(".slide-in-obsrvr-init").forEach((sec) => {
      this.addInterSect("slide-in-obsrvr").observe(sec);
    });
    document.querySelectorAll(".from-right-init").forEach((sec) => {
      this.addInterSect("from-right", { rootMargin: "0px" }).observe(sec);
    });
  }
  addInterSect(
    class_,
    options = {
      rootMargin: "-150px",
      threshold: 0,
    }
  ) {
    return new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        entry.isIntersecting
          ? entry.target.classList.add(class_)
          : entry.target.classList.remove(class_);
      });
    }, options);
  }
}

class sidebarContent {
  constructor() {}
  async sendRequest() {
    const url = `/api/get-side-view/`;
    await blueRex
      .get(url)
      .then((res) => {
        res = JSON.parse(res);
        this.showDataInPage(res);
        return 1;
      })
      .catch((e) => {
        console.error(e);
      });
  }
  showDataInPage(data) {
    const view = document.querySelector("#side-bar-data");
    view.innerHTML = "";
    if (data.products) {
      const title = `MOST RECENT PRODUCTS`;
      let html = `<div class="blog-right-in fade-in">`;
      html += `<h3>${title}</h3><div class="items98883293">`;
      data.products.map((item) => {
        html += this.setTemplate(item);
      });
      html += `<div></div>`;
      view.innerHTML = html;
    }
    if (data.category_list) {
      const title = `TOP CATEGORIES`;
      let html = `<div class="blog-right-in fade-in">`;
      html += `<h3>${title}</h3><ul class="ul-8883kskx">`;
      data.category_list.map((item) => {
        html += `<li><a href="/products/category/${item.slug}">${item.name}</a></li>`;
      });
      html += `</ul></div>`;
      view.innerHTML += html;
    }
    if (data.blogs) {
      const title = `READ NEW BLOGS`;
      let html = `<div class="blog-right-in fade-in blogs-view-23332cj">`;
      html += `<h3>${title}</h3><div class="blog-llll"`;
      data.blogs.map((item) => {
        html += this.setTemplate(item, "blogs");
      });
      html += `</div></div>`;
      view.innerHTML += html;
    }
  }
  setTemplate(item, type = "") {
    return `
            <a class="side-bar-item-links " href="${
              type == "blogs" ? "/blogs/" : "/products/"
            }${item.slug}" title="Buy ${item.title}">
                <section class="df ac">
                    <div class="left-acc">
                        <img
                            src="${
                              item.image == ""
                                ? item.image_link
                                : `/media/${item.image}`
                            }"
                            alt="${item.title}"
                        />
                        ${
                          item.isNew ? '<span class="new-badge side-bar-sec1224">New</span>' : ""
                        }
                        
                        </div>
                        <div class="uryal">
                        <h3>${item.title}</h3>
                        ${
                          type == "blogs"
                            ? ` <span>${item.author} - ${new Date(
                                item.createdAt
                              ).getDate()}/${new Date(
                                item.createdAt
                              ).getMonth()}/${new Date(
                                item.createdAt
                              ).getFullYear()}</span>`
                            : `
                            <div>
                              <div class="yellow-roar">
                                  <span class="abc-dd3la2">in just <i class="fa fa-usd"></i>${item.price}</span>
                                  <a href="/products/${item.slug}" class="db side-bar-link">Buy Product</a>
                              </div>
                              ${
                                item.views ? ` <div class="views-counter mashar urckc" style="display:inline">
                                <i class="fa fa-eye"></i> 
                                <span>${item.views}</span>
                              </div>` : ""
                            }
                                </div>`
                        }
                    
                    </div>
                </section>
            </a>
        `;
  }
}
if (document.querySelector("#side-bar-data")) {
  const sidebar = new sidebarContent();
  sidebar.sendRequest();
}
document.addEventListener("DOMContentLoaded", () => {
  new IntersectingLazyLoading();
  new IntersectingStyles();
});

if (document.querySelector("#load-tags-data")) {
  new LoadTagsData();
}
