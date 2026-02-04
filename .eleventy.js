module.exports = function (eleventyConfig) {
  eleventyConfig.setTemplateFormats(["html", "njk"]);
  eleventyConfig.addPassthroughCopy("wp-content");
  eleventyConfig.addPassthroughCopy("wp-includes");
  eleventyConfig.addPassthroughCopy("fonts");
  eleventyConfig.addPassthroughCopy("comments");
  eleventyConfig.addPassthroughCopy("2021");
  eleventyConfig.addPassthroughCopy("05");
  eleventyConfig.addPassthroughCopy("CNAME");

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
