module.exports = function (eleventyConfig) {
  const basePath = (process.env.ELEVENTY_BASE_PATH || "").trim().replace(/\/+$/, "");
  const basePathNoSlash = basePath.replace(/^\//, "");

  if (basePathNoSlash) {
    const esc = basePathNoSlash.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const prefix = basePath;
    eleventyConfig.addTransform("prefix-base-path", function (content, outputPath) {
      if (!outputPath || !outputPath.endsWith(".html")) {
        return content;
      }

      // Prefix absolute-root URLs so GitHub Pages subpath works.
      let out = content;
      out = out.replace(
        new RegExp(`\\b(href|src)=(\"|')/(?!/|${esc}/)([^\"']+)`, "g"),
        `$1=$2${prefix}/$3`
      );
      out = out.replace(
        new RegExp(`url\\(\\s*\"?/(?!/|${esc}/)`, "g"),
        `url(${prefix}/`
      );
      return out;
    });
  }
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
