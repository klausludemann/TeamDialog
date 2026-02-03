module.exports = function (eleventyConfig) {
  eleventyConfig.setTemplateFormats(["html", "njk"]);
  eleventyConfig.addPassthroughCopy("wp-content");
  eleventyConfig.addPassthroughCopy("wp-includes");
  eleventyConfig.addPassthroughCopy("fonts");
  eleventyConfig.addPassthroughCopy("comments");
  eleventyConfig.addPassthroughCopy("2021");
  eleventyConfig.addPassthroughCopy("05");
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy({ "index4121.html": "index4121.html" });
  eleventyConfig.addPassthroughCopy({ "index59a1.html": "index59a1.html" });
  eleventyConfig.addPassthroughCopy({ "index6225.html": "index6225.html" });
  eleventyConfig.addPassthroughCopy({ "index735e.html": "index735e.html" });
  eleventyConfig.addPassthroughCopy({ "index8769.html": "index8769.html" });
  eleventyConfig.addPassthroughCopy({ "index926d.html": "index926d.html" });
  eleventyConfig.addPassthroughCopy({ "index9f84.html": "index9f84.html" });
  eleventyConfig.addPassthroughCopy({ "indexd188.html": "indexd188.html" });
  eleventyConfig.addPassthroughCopy({ "indexe614.html": "indexe614.html" });
  eleventyConfig.addPassthroughCopy({ "indexe8f3.html": "indexe8f3.html" });

  return {
    dir: {
      input: "site/src/pages",
      includes: "../_includes",
      data: "../_data",
      output: "docs",
    },
    htmlTemplateEngine: "njk",
  };
};
