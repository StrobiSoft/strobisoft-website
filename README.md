# StrobiSoft website

Official company website for **StrobiSoft**, including the standalone NODE IJET technology section and its public-facing technical specification.

**Target domain:** `https://strobisoft.com/`  
**NODE IJET:** `https://strobisoft.com/node-ijet/`

## Distribution and intellectual property

The repository contains **only the public website's static HTML and CSS**. It does not contain the proprietary NODE IJET implementation, internal ZooLab configuration, keys, runtime files, or private agent/robot infrastructure. The NODE IJET source remains in a separate **private** development repository.

Third-party technology **Vetto** is credited to its original creator `shleder`. Vetto-based monitoring and automated quarantine are future integration objectives, not marketed as verified production capabilities.

© 2026 StrobiSoft. All rights reserved.

## Publishing with GitHub Pages

1. Open [Settings → Pages](https://github.com/StrobiSoft/strobisoft-website/settings/pages).
2. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, then **Save**.
3. Verify the temporary Pages site is reachable as `https://strobisoft.github.io/strobisoft-website/`.
4. Configure **Custom domain** as `strobisoft.com` using the repository Pages settings; GitHub writes a `CNAME` file in branch publishing mode.
5. At the DNS provider, point the root `@` to GitHub Pages' published IPv4 addresses, without changing nameservers, unrelated subdomains, mail records, or third-party services. Official documentation: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site .
6. Enable **Enforce HTTPS** when the certificate is available, verify both the homepage and NODE IJET subpage from outside the home network, then update old promotional links.

Do not substitute the `192.168.1.154` private VM110 IP address in public DNS. The separate Pepper VM110 site is LAN-only staging and backup, not the public Pages server.
