# Add ClimateNatureAI to WordPress.com

1. Publish the dashboard to GitHub Pages first.
2. In WordPress.com, open Pages and edit the CTCNA page where the dashboard should appear.
3. Add a Custom HTML block.
4. Paste `climatenatureai-embed.html` after replacing the iframe URL if your published path differs.
5. Preview on desktop and mobile, then publish.
6. If WordPress removes the iframe, check the site's plan and whether hosting features are activated. WordPress.com restricts iframe/script tags on sites without the required plan features. Use a normal link/button to open the dashboard in a new tab as a fallback.
7. Do not point `ctcna.org` at GitHub Pages if it is still intended to serve the WordPress.com website. Keep the dashboard on its GitHub Pages URL or a separate subdomain.

Official WordPress.com guidance: https://wordpress.com/support/code/ and https://wordpress.com/support/wordpress-editor/blocks/custom-html-block/
