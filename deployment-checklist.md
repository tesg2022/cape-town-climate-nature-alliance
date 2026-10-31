# Deployment checklist

## GitHub
- Confirm repository exists and that you have admin/write permission.
- Copy `site/` to `climatenatureai/` at repository root.
- Copy `.github/workflows/pages.yml` to repository `.github/workflows/pages.yml`.
- Enable GitHub Pages: Settings -> Pages -> Build and deployment -> GitHub Actions.
- Push to `main`; check Actions and open the published Pages URL.
- Ensure `climatenatureai/index.html` is served at `/climatenatureai/`.

## WordPress.com
- Add a page titled ClimateNatureAI Environmental Assessment.
- Add the iframe snippet only if the WordPress.com plan and hosting features allow it.
- Otherwise use a link/button to the dashboard in a new tab.
- Keep ctcna.org on WordPress.com if it is already configured there; do not change DNS as part of this dashboard deployment.

## Before public release
- Confirm source data publication rights and approvals.
- Review whether any coordinates, stakeholder information, draft financial information or internal review records are sensitive.
- Validate study boundary and data provenance.
- Verify units and model evaluation design.
- Label exploratory trend outputs and all simulated/model-derived outputs.
- Do not claim intervention effectiveness or regulatory approval.
