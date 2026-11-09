# modernpmo.ca

Static website for **ModernPMO Consulting and Technology LTD.**, hosted on GitHub Pages at https://modernpmo.ca.

| Path | Purpose |
|---|---|
| `index.html`, `pt/index.html` | Home page (English / Portuguese) |
| `terms.html`, `refund-policy.html`, `privacy.html`, `payments.html` | Legal & payment pages (EN) |
| `pt/termos.html`, `pt/reembolso.html`, `pt/privacidade.html`, `pt/pagamentos.html` | Legal & payment pages (PT) |
| `thanks.html`, `pt/obrigado.html` | Form confirmation pages |
| `tools/build_pages.py` | Generates the legal + thank-you pages. Edit content there, then run `python tools/build_pages.py` |
| `CNAME` | Custom domain for GitHub Pages |

The service request form posts to [FormSubmit](https://formsubmit.co). The first submission sends an activation email to the receiving address. Click it once to activate.

No build step for the home pages. Edit the HTML and push to `main` to publish.

## Free PMO assessment

The "Free assessment" / "Diagnóstico gratuito" section links to the assessment app at
`https://assessment.modernpmo.ca/en` (English) and `https://assessment.modernpmo.ca/` (Portuguese).
The app is a separate Next.js project (repo `PMO-Hub`, folder `Code PMO Assessment/modernpmo-mvp/modernpmo`)
hosted on Vercel. **Deploy it and point the `assessment` CNAME at Vercel before publishing these links.**
