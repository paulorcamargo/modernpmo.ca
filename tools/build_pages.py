"""Generates the legal and thank-you pages (EN + PT) from one template.

Run from the repo root:  python tools/build_pages.py
Edit the CONTENT below, then re-run and commit the generated .html files.
"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIZ = "ModernPMO Consulting and Technology LTD."
ADDR = "52 Macewan Ridge Close NW, Calgary, Alberta T3K 3G6"
EMAIL = "paulo.camargo@modernpmo.com"
UPDATED = {"en": "Last updated: October 6, 2026", "pt": "Última atualização: 6 de outubro de 2026"}

CARD_MARKS = (
    '<div class="card-marks" aria-label="Visa, Mastercard">'
    '<svg viewBox="0 0 64 40" role="img" aria-label="Visa"><rect width="64" height="40" rx="5" fill="#fff"/>'
    '<text x="32" y="27" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="17" '
    'font-weight="900" font-style="italic" fill="#1A1F71">VISA</text></svg>'
    '<svg viewBox="0 0 64 40" role="img" aria-label="Mastercard"><rect width="64" height="40" rx="5" fill="#fff"/>'
    '<circle cx="26" cy="20" r="11" fill="#EB001B"/><circle cx="38" cy="20" r="11" fill="#F79E1B"/>'
    '<path d="M32 10.8a11 11 0 0 1 0 18.4a11 11 0 0 1 0-18.4z" fill="#FF5F00"/></svg></div>'
)

L = {
    "en": dict(
        html_lang="en", home="/", other="/pt/", other_label="PT", other_lang="pt",
        back="← Back to home", rights="All rights reserved.", country="Canada",
        links=[("/terms.html", "Terms &amp; Conditions"), ("/refund-policy.html", "Refund &amp; Cancellation"),
               ("/privacy.html", "Privacy Policy"), ("/payments.html", "Payments &amp; Security"),
               ("/pt/", "Português")],
    ),
    "pt": dict(
        html_lang="pt-BR", home="/pt/", other="/", other_label="EN", other_lang="en",
        back="← Voltar ao início", rights="Todos os direitos reservados.", country="Canadá",
        links=[("/pt/termos.html", "Termos e Condições"), ("/pt/reembolso.html", "Reembolso e Cancelamento"),
               ("/pt/privacidade.html", "Privacidade"), ("/pt/pagamentos.html", "Pagamentos e Segurança"),
               ("/", "English")],
    ),
}


def page(lang, path, title, body, other_path=None, legal=True):
    c = L[lang]
    footer_links = "\n        ".join(f'<a href="{h}">{t}</a>' for h, t in c["links"])
    updated = f'<p class="updated">{UPDATED[lang]}</p>' if legal else ""
    return f"""<!DOCTYPE html>
<html lang="{c['html_lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ModernPMO</title>
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&family=Manrope:wght@300;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
  <header class="site-header">
    <nav class="container nav">
      <a href="{c['home']}" class="logo"><span class="logo-mark">M</span><span>Modern<span class="dot">PMO</span></span></a>
      <ul class="nav-links" style="display:flex;position:static;flex-direction:row;padding:0;border:0;background:none">
        <li><a href="{c['home']}">{c['back']}</a></li>
        <li><a href="{other_path or c['other']}" class="lang-switch" hreflang="{c['other_lang']}">{c['other_label']}</a></li>
      </ul>
    </nav>
  </header>
  <main class="container legal">
    <h1>{title}</h1>
    {updated}
{body}
  </main>
  <footer class="site-footer">
    <div class="container footer-inner">
      <div>
        <strong>{BIZ}</strong><br>
        {ADDR}, {c['country']}<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        © <span id="year"></span> {BIZ} {c['rights']}
      </div>
      <nav class="footer-legal">
        {footer_links}
      </nav>
    </div>
  </footer>
  <script src="/assets/main.js"></script>
</body>
</html>
"""


CONTACT_EN = f"""<p>{BIZ}<br>{ADDR}, Canada<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""
CONTACT_PT = f"""<p>{BIZ}<br>{ADDR}, Canadá<br>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""

# ---------------------------------------------------------------- TERMS
TERMS_EN = f"""
    <p>These Terms &amp; Conditions ("Terms") apply to all consulting, implementation, mentoring and training services ("Services") provided by {BIZ} ("ModernPMO", "we", "us"), a company based in Calgary, Alberta, Canada, to the client named in a proposal ("Client", "you").</p>

    <h2>1. Services</h2>
    <p>Our Services include PMO diagnostics, PMO implementation and improvement, PMO consulting and interim PMO leadership, PMIS (Project Management Information System) implementation, portfolio management, governance and methodology, reporting and Power BI dashboards, mentoring and coaching, and training courses (including project management, productivity with Microsoft 365 and Microsoft tools, and AI tools). Services are professional services. No physical goods are sold or shipped.</p>
    <p>The exact scope, deliverables, schedule, format (remote or on-site) and fees of each engagement are described in a written proposal or statement of work ("Proposal").</p>

    <h2>2. Requests, proposals and acceptance</h2>
    <ul>
      <li>Submitting a service request through our website is free and creates no obligation for either party.</li>
      <li>A Proposal is valid for 30 days unless it states otherwise.</li>
      <li>An agreement is formed when you accept a Proposal in writing (signature, email confirmation or electronic acceptance). By accepting, you confirm that you have read and accept these Terms and our <a href="/refund-policy.html">Refund &amp; Cancellation Policy</a>.</li>
      <li>If a Proposal conflicts with these Terms, the Proposal prevails for that engagement.</li>
    </ul>

    <h2>3. Fees, currency and payment</h2>
    <ul>
      <li>All fees are quoted and charged in <strong>Canadian dollars (CAD, $)</strong>, unless the Proposal expressly states another currency.</li>
      <li>Fees are either fixed (fixed-fee engagements) or based on hours worked at the rates stated in the Proposal (time-and-materials engagements). Monthly advisory and mentoring are billed monthly in advance.</li>
      <li>Applicable taxes, such as the federal Goods and Services Tax (GST), are added where required by law.</li>
      <li>Fixed-fee engagements may require a deposit of up to 50% on acceptance, with the balance invoiced on milestones or completion as stated in the Proposal.</li>
      <li>Invoices are payable within 15 days unless the Proposal states otherwise. Payment can be made by Visa or Mastercard through the secure checkout of our payment provider, Wise, or by bank transfer. See <a href="/payments.html">Payments, Delivery &amp; Security</a>.</li>
      <li>Pre-approved travel expenses for on-site work are invoiced at cost, only if stated in the Proposal.</li>
    </ul>

    <h2>4. Delivery</h2>
    <p>Services are delivered remotely (video conference) or on-site at the location agreed in the Proposal, according to the schedule in the Proposal. Documents, reports, configurations and dashboards are delivered electronically. Delivery dates depend on timely access to your people, information and systems.</p>

    <h2>5. Client responsibilities</h2>
    <p>You agree to provide timely access to stakeholders, information, systems and decisions reasonably needed for the Services. You are responsible for licences and subscriptions to third-party software (for example, a PMIS/PPM platform or Microsoft Power BI), which you purchase directly from the vendor under the vendor's terms.</p>

    <h2>6. Changes</h2>
    <p>Changes to scope, schedule or deliverables must be agreed in writing and may change the fees and timeline.</p>

    <h2>7. Intellectual property</h2>
    <p>On full payment, you own the deliverables created specifically for you. ModernPMO keeps ownership of its pre-existing methods, frameworks, templates and know-how, and grants you a perpetual, non-exclusive licence to use them inside your organization as part of the deliverables.</p>

    <h2>8. Confidentiality</h2>
    <p>Each party will keep the other's confidential information confidential and use it only to perform or receive the Services. This obligation continues for 3 years after the engagement ends.</p>

    <h2>9. No guarantee of outcomes</h2>
    <p>We perform the Services with professional care and skill. Business results depend on factors outside our control, so we do not guarantee specific outcomes such as savings, adoption levels or project success.</p>

    <h2>10. Limitation of liability</h2>
    <p>To the extent permitted by law, ModernPMO's total liability for any claim related to an engagement is limited to the fees paid by you for that engagement in the 12 months before the claim. Neither party is liable for indirect, consequential or lost-profit damages.</p>

    <h2>11. Cancellation, termination and refunds</h2>
    <p>Cancellation, termination and refunds are governed by our <a href="/refund-policy.html">Refund &amp; Cancellation Policy</a>, which forms part of these Terms.</p>

    <h2>12. Export restrictions and sanctions</h2>
    <p>Our Services are subject to Canadian export control and economic sanctions laws, including the <em>Special Economic Measures Act</em> and the <em>Export and Import Permits Act</em>. We do not provide Services to persons, entities or jurisdictions subject to Canadian sanctions, and we may decline or end an engagement where providing the Services would breach these laws. You must not use our deliverables in violation of applicable export or sanctions laws.</p>

    <h2>13. Governing law</h2>
    <p>These Terms are governed by the laws of the Province of Alberta and the federal laws of Canada that apply there. The courts of Calgary, Alberta have exclusive jurisdiction, subject to any mandatory consumer protection rights you may have.</p>

    <h2>14. Changes to these Terms</h2>
    <p>We may update these Terms from time to time. The version in force when you accept a Proposal applies to that engagement.</p>

    <h2>15. Contact</h2>
    {CONTACT_EN}
"""

TERMS_PT = f"""
    <p>Estes Termos e Condições ("Termos") se aplicam a todos os serviços de consultoria, implantação, mentoria e treinamento ("Serviços") prestados pela {BIZ} ("ModernPMO", "nós"), empresa sediada em Calgary, Alberta, Canadá, ao cliente indicado em uma proposta ("Cliente", "você"). Esta é uma tradução; em caso de divergência, prevalece a <a href="/terms.html">versão em inglês</a>.</p>

    <h2>1. Serviços</h2>
    <p>Nossos Serviços incluem diagnóstico de PMO, implantação e melhoria de PMO, consultoria e liderança interina de PMO, implantação de PMIS (Sistema de Informações de Gerenciamento de Projetos), gestão de portfólio, governança e metodologia, relatórios e dashboards em Power BI, mentoria e coaching, e cursos de treinamento (incluindo gerenciamento de projetos, produtividade com Microsoft 365 e ferramentas Microsoft, e ferramentas de IA). Os Serviços são serviços profissionais. Nenhum produto físico é vendido ou enviado.</p>
    <p>O escopo, os entregáveis, o cronograma, o formato (remoto ou presencial) e os valores de cada projeto são descritos em uma proposta ou declaração de trabalho por escrito ("Proposta").</p>

    <h2>2. Solicitações, propostas e aceite</h2>
    <ul>
      <li>O envio de uma solicitação de serviço pelo site é gratuito e não gera obrigação para nenhuma das partes.</li>
      <li>A Proposta é válida por 30 dias, salvo indicação em contrário.</li>
      <li>O acordo é formado quando você aceita a Proposta por escrito (assinatura, confirmação por e-mail ou aceite eletrônico). Ao aceitar, você confirma que leu e aceita estes Termos e a nossa <a href="/pt/reembolso.html">Política de Reembolso e Cancelamento</a>.</li>
      <li>Se a Proposta conflitar com estes Termos, a Proposta prevalece para aquele projeto.</li>
    </ul>

    <h2>3. Valores, moeda e pagamento</h2>
    <ul>
      <li>Todos os valores são cotados e cobrados em <strong>dólares canadenses (CAD, $)</strong>, salvo se a Proposta indicar expressamente outra moeda.</li>
      <li>Os valores são fixos (projetos de preço fixo) ou baseados em horas trabalhadas às taxas indicadas na Proposta (tempo e materiais). Advisory e mentoria mensais são cobrados mensalmente de forma antecipada.</li>
      <li>Tributos aplicáveis, como o imposto federal canadense GST, são acrescidos quando exigidos por lei.</li>
      <li>Projetos de preço fixo podem exigir um sinal de até 50% no aceite, com o saldo faturado por marcos ou na conclusão, conforme a Proposta.</li>
      <li>As faturas vencem em 15 dias, salvo indicação diferente na Proposta. O pagamento pode ser feito com Visa ou Mastercard pelo checkout seguro do nosso provedor de pagamentos, a Wise, ou por transferência bancária. Veja <a href="/pt/pagamentos.html">Pagamentos, Entrega e Segurança</a>.</li>
      <li>Despesas de viagem pré-aprovadas para trabalho presencial são faturadas pelo custo, somente se previstas na Proposta.</li>
    </ul>

    <h2>4. Entrega</h2>
    <p>Os Serviços são prestados de forma remota (videoconferência) ou presencial, no local acordado na Proposta, conforme o cronograma da Proposta. Documentos, relatórios, configurações e dashboards são entregues eletronicamente. As datas de entrega dependem do acesso oportuno a pessoas, informações e sistemas do Cliente.</p>

    <h2>5. Responsabilidades do Cliente</h2>
    <p>Você se compromete a fornecer, em tempo hábil, acesso a stakeholders, informações, sistemas e decisões razoavelmente necessários aos Serviços. Licenças e assinaturas de softwares de terceiros (por exemplo, uma plataforma de PMIS/PPM ou o Microsoft Power BI) são de sua responsabilidade e adquiridas diretamente do fornecedor, conforme os termos dele.</p>

    <h2>6. Alterações</h2>
    <p>Alterações de escopo, prazo ou entregáveis devem ser acordadas por escrito e podem alterar valores e cronograma.</p>

    <h2>7. Propriedade intelectual</h2>
    <p>Após o pagamento integral, você passa a ser titular dos entregáveis criados especificamente para você. A ModernPMO mantém a titularidade de seus métodos, frameworks, templates e know-how preexistentes e concede a você uma licença perpétua e não exclusiva para usá-los internamente como parte dos entregáveis.</p>

    <h2>8. Confidencialidade</h2>
    <p>Cada parte manterá em sigilo as informações confidenciais da outra e as usará apenas para prestar ou receber os Serviços. Esta obrigação permanece por 3 anos após o término do projeto.</p>

    <h2>9. Sem garantia de resultados</h2>
    <p>Prestamos os Serviços com zelo e competência profissional. Resultados de negócio dependem de fatores fora do nosso controle, por isso não garantimos resultados específicos, como economias, níveis de adoção ou sucesso de projetos.</p>

    <h2>10. Limitação de responsabilidade</h2>
    <p>Na extensão permitida por lei, a responsabilidade total da ModernPMO por qualquer reclamação relacionada a um projeto fica limitada aos valores pagos por você por aquele projeto nos 12 meses anteriores à reclamação. Nenhuma das partes responde por danos indiretos, consequenciais ou lucros cessantes.</p>

    <h2>11. Cancelamento, rescisão e reembolsos</h2>
    <p>Cancelamentos, rescisões e reembolsos seguem a nossa <a href="/pt/reembolso.html">Política de Reembolso e Cancelamento</a>, que faz parte destes Termos.</p>

    <h2>12. Restrições de exportação e sanções</h2>
    <p>Nossos Serviços estão sujeitos às leis canadenses de controle de exportação e sanções econômicas, incluindo o <em>Special Economic Measures Act</em> e o <em>Export and Import Permits Act</em>. Não prestamos Serviços a pessoas, entidades ou jurisdições sujeitas a sanções canadenses e podemos recusar ou encerrar um projeto se sua execução violar essas leis. Você não deve usar nossos entregáveis em violação às leis de exportação ou sanções aplicáveis.</p>

    <h2>13. Lei aplicável</h2>
    <p>Estes Termos são regidos pelas leis da Província de Alberta e pelas leis federais do Canadá aplicáveis. Fica eleito o foro de Calgary, Alberta, ressalvados direitos obrigatórios de proteção ao consumidor que você possa ter.</p>

    <h2>14. Alterações destes Termos</h2>
    <p>Podemos atualizar estes Termos periodicamente. A versão vigente no momento do aceite da Proposta se aplica àquele projeto.</p>

    <h2>15. Contato</h2>
    {CONTACT_PT}
"""

# ---------------------------------------------------------------- REFUND
REFUND_EN = f"""
    <p>This policy explains how you can cancel, reschedule or end an engagement with {BIZ} and when refunds apply. <strong>Please read it before accepting a proposal.</strong> Our refund policy is limited as described below, and by accepting a proposal you confirm that you accept it.</p>

    <h2>1. Service requests and proposals</h2>
    <p>Requesting a proposal is free. Nothing is charged until you accept a written proposal and receive an invoice.</p>

    <h2>2. Cancellation before the engagement starts</h2>
    <ul>
      <li><strong>10 or more business days</strong> before the scheduled start date: full refund of all amounts paid.</li>
      <li><strong>5 to 9 business days</strong> before the start date: refund of 50% of the deposit.</li>
      <li><strong>Less than 5 business days</strong> before the start date: the deposit is non-refundable, but it can be credited once to a new start date within 90 days.</li>
    </ul>

    <h2>3. Workshops and training sessions</h2>
    <p>You can reschedule a workshop or training session once at no cost with at least 5 business days' written notice. Cancellations follow section 2. Sessions missed without notice are not refundable.</p>

    <h2>4. Termination after work has started</h2>
    <p>Either party may end an engagement with 10 business days' written notice. You pay for work performed and expenses incurred up to the termination date. Any amount you prepaid for work not yet performed is refunded.</p>

    <h2>5. Monthly advisory and mentoring</h2>
    <p>Monthly services can be cancelled at any time by email. Cancellation takes effect at the end of the current billing month, and no further charges apply. The current month is not refunded on a pro-rated basis.</p>

    <h2>6. Cancellation by ModernPMO</h2>
    <p>If we cancel or cannot deliver a scheduled service, we will offer a new date. If you do not accept it, we refund 100% of the amounts paid for the undelivered services.</p>

    <h2>7. Satisfaction with deliverables</h2>
    <p>If a deliverable does not meet the scope agreed in the proposal, tell us in writing within 10 business days of delivery. We will correct it at no additional cost. If we cannot correct it, we will refund the portion of the fee related to that deliverable.</p>

    <h2>8. How refunds are paid</h2>
    <ul>
      <li>Refunds are issued in Canadian dollars (CAD, $) to the original payment method (card or bank account) within 10 business days of approval.</li>
      <li>Card refunds can take a further 5 to 10 business days to appear, depending on your card issuer.</li>
      <li>We are not responsible for currency conversion differences or fees charged by your bank or card issuer.</li>
    </ul>

    <h2>9. How to cancel or request a refund</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your name, organization, proposal or invoice number and the reason for your request. We reply within 2 business days. Please contact us before disputing a charge with your card issuer, because most issues can be resolved quickly.</p>

    <h2>10. Contact</h2>
    {CONTACT_EN}
"""

REFUND_PT = f"""
    <p>Esta política explica como você pode cancelar, remarcar ou encerrar um projeto com a {BIZ} e quando há reembolso. <strong>Leia antes de aceitar uma proposta.</strong> Nossa política de reembolso é limitada conforme descrito abaixo, e ao aceitar uma proposta você confirma que a aceita. Esta é uma tradução; em caso de divergência, prevalece a <a href="/refund-policy.html">versão em inglês</a>.</p>

    <h2>1. Solicitações e propostas</h2>
    <p>Solicitar uma proposta é gratuito. Nada é cobrado até que você aceite uma proposta por escrito e receba uma fatura.</p>

    <h2>2. Cancelamento antes do início</h2>
    <ul>
      <li><strong>10 ou mais dias úteis</strong> antes da data de início: reembolso integral dos valores pagos.</li>
      <li><strong>5 a 9 dias úteis</strong> antes do início: reembolso de 50% do sinal.</li>
      <li><strong>Menos de 5 dias úteis</strong> antes do início: o sinal não é reembolsável, mas pode ser usado uma vez como crédito para uma nova data em até 90 dias.</li>
    </ul>

    <h2>3. Workshops e treinamentos</h2>
    <p>Você pode remarcar um workshop ou treinamento uma vez, sem custo, com pelo menos 5 dias úteis de aviso por escrito. Cancelamentos seguem a seção 2. Sessões perdidas sem aviso não são reembolsáveis.</p>

    <h2>4. Rescisão após o início do trabalho</h2>
    <p>Qualquer parte pode encerrar o projeto com 10 dias úteis de aviso por escrito. Você paga pelo trabalho realizado e despesas incorridas até a data da rescisão. Valores pagos antecipadamente por trabalho ainda não realizado são reembolsados.</p>

    <h2>5. Advisory e mentoria mensais</h2>
    <p>Serviços mensais podem ser cancelados a qualquer momento por e-mail. O cancelamento vale a partir do fim do mês de faturamento corrente, sem cobranças posteriores. O mês corrente não é reembolsado proporcionalmente.</p>

    <h2>6. Cancelamento pela ModernPMO</h2>
    <p>Se cancelarmos ou não pudermos prestar um serviço agendado, ofereceremos uma nova data. Caso você não aceite, reembolsamos 100% dos valores pagos pelos serviços não prestados.</p>

    <h2>7. Satisfação com os entregáveis</h2>
    <p>Se um entregável não atender ao escopo acordado na proposta, avise-nos por escrito em até 10 dias úteis após a entrega. Faremos a correção sem custo adicional. Se não for possível corrigir, reembolsaremos a parte do valor referente àquele entregável.</p>

    <h2>8. Como os reembolsos são pagos</h2>
    <ul>
      <li>Os reembolsos são feitos em dólares canadenses (CAD, $) para o meio de pagamento original (cartão ou conta bancária) em até 10 dias úteis após a aprovação.</li>
      <li>Reembolsos em cartão podem levar mais 5 a 10 dias úteis para aparecer, conforme o emissor do cartão.</li>
      <li>Não nos responsabilizamos por diferenças de conversão cambial ou tarifas cobradas pelo seu banco ou emissor do cartão.</li>
    </ul>

    <h2>9. Como cancelar ou pedir reembolso</h2>
    <p>Envie um e-mail para <a href="mailto:{EMAIL}">{EMAIL}</a> com seu nome, organização, número da proposta ou fatura e o motivo. Respondemos em até 2 dias úteis. Entre em contato conosco antes de contestar uma cobrança junto ao emissor do cartão, pois a maioria das questões é resolvida rapidamente.</p>

    <h2>10. Contato</h2>
    {CONTACT_PT}
"""

# ---------------------------------------------------------------- PRIVACY
PRIVACY_EN = f"""
    <p>{BIZ} respects your privacy and handles personal information in accordance with Canada's <em>Personal Information Protection and Electronic Documents Act</em> (PIPEDA) and Alberta's <em>Personal Information Protection Act</em> (PIPA).</p>

    <h2>1. Information we collect</h2>
    <ul>
      <li><strong>Service requests:</strong> name, work email, organization, phone (optional), service of interest, preferred start date and your message.</li>
      <li><strong>Engagements:</strong> business contact details and information needed to deliver the Services and to invoice.</li>
      <li><strong>Payments:</strong> card payments are processed by our payment provider, Wise. We do <strong>not</strong> receive or store your full card number, expiry date or security code.</li>
      <li><strong>Technical data:</strong> our hosting provider (GitHub Pages) and font provider (Google Fonts) may process your IP address and browser information to deliver the website. We do not use advertising or analytics cookies.</li>
    </ul>

    <h2>2. How we use it</h2>
    <p>We use personal information to respond to your request, prepare proposals, deliver and invoice Services, process payments and refunds, and meet legal and tax obligations. We do not sell or rent personal information, and we do not use it for unrelated marketing without your consent.</p>

    <h2>3. Service providers</h2>
    <p>We share information only with providers that help us operate: FormSubmit (delivery of website form submissions by email), Wise (payment processing), GitHub (website hosting), and our email and accounting providers. Some of these providers may process information outside Canada, for example in the United States or the European Union, where it may be accessible under local law.</p>

    <h2>4. Retention</h2>
    <p>Service requests that do not become engagements are deleted within 24 months. Client and billing records are kept for as long as required by Canadian tax law (generally 6 years).</p>

    <h2>5. Security</h2>
    <p>The website is served only over encrypted HTTPS. Access to personal information is limited to people who need it. See <a href="/payments.html">Payments, Delivery &amp; Security</a> for how card details are protected.</p>

    <h2>6. Your rights</h2>
    <p>You can ask to access or correct your personal information, or withdraw consent (subject to legal or contractual limits), by emailing our Privacy Officer at <a href="mailto:{EMAIL}">{EMAIL}</a>. If you are not satisfied with our response, you may contact the Office of the Privacy Commissioner of Canada or the Office of the Information and Privacy Commissioner of Alberta.</p>

    <h2>7. Contact</h2>
    {CONTACT_EN}
"""

PRIVACY_PT = f"""
    <p>A {BIZ} respeita a sua privacidade e trata informações pessoais de acordo com a lei canadense <em>Personal Information Protection and Electronic Documents Act</em> (PIPEDA) e a lei de Alberta <em>Personal Information Protection Act</em> (PIPA). Esta é uma tradução; em caso de divergência, prevalece a <a href="/privacy.html">versão em inglês</a>.</p>

    <h2>1. Informações que coletamos</h2>
    <ul>
      <li><strong>Solicitações de serviço:</strong> nome, e-mail corporativo, organização, telefone (opcional), serviço de interesse, início desejado e sua mensagem.</li>
      <li><strong>Projetos:</strong> dados de contato comerciais e informações necessárias para prestar os Serviços e faturar.</li>
      <li><strong>Pagamentos:</strong> pagamentos com cartão são processados pelo nosso provedor de pagamentos, a Wise. <strong>Não</strong> recebemos nem armazenamos o número completo, a validade ou o código de segurança do seu cartão.</li>
      <li><strong>Dados técnicos:</strong> nosso provedor de hospedagem (GitHub Pages) e de fontes (Google Fonts) podem tratar seu endereço IP e dados do navegador para entregar o site. Não usamos cookies de publicidade ou de analytics.</li>
    </ul>

    <h2>2. Como usamos</h2>
    <p>Usamos as informações para responder à sua solicitação, preparar propostas, prestar e faturar os Serviços, processar pagamentos e reembolsos e cumprir obrigações legais e fiscais. Não vendemos nem alugamos informações pessoais e não as usamos para marketing não relacionado sem o seu consentimento.</p>

    <h2>3. Prestadores de serviço</h2>
    <p>Compartilhamos informações apenas com prestadores que nos ajudam a operar: FormSubmit (envio por e-mail dos formulários do site), Wise (processamento de pagamentos), GitHub (hospedagem do site) e nossos provedores de e-mail e contabilidade. Alguns podem tratar informações fora do Canadá, por exemplo nos Estados Unidos ou na União Europeia, onde podem estar acessíveis conforme a lei local.</p>

    <h2>4. Retenção</h2>
    <p>Solicitações que não se tornam projetos são excluídas em até 24 meses. Registros de clientes e faturamento são mantidos pelo prazo exigido pela legislação fiscal canadense (em geral, 6 anos).</p>

    <h2>5. Segurança</h2>
    <p>O site é servido somente por HTTPS criptografado. O acesso a informações pessoais é restrito a quem precisa delas. Veja <a href="/pt/pagamentos.html">Pagamentos, Entrega e Segurança</a> para saber como os dados de cartão são protegidos.</p>

    <h2>6. Seus direitos</h2>
    <p>Você pode solicitar acesso ou correção das suas informações pessoais, ou retirar o consentimento (respeitados limites legais ou contratuais), escrevendo ao nosso Encarregado de Privacidade em <a href="mailto:{EMAIL}">{EMAIL}</a>. Se não estiver satisfeito com a resposta, pode contatar o Office of the Privacy Commissioner of Canada ou o Office of the Information and Privacy Commissioner of Alberta.</p>

    <h2>7. Contato</h2>
    {CONTACT_PT}
"""

# ---------------------------------------------------------------- PAYMENTS
PAYMENTS_EN = f"""
    <p>This page explains how to pay for our Services, how they are delivered, and how your payment information is protected.</p>

    <h2>1. Business location</h2>
    <p>{BIZ} is a business <strong>based in Canada</strong>. Our permanent business address is {ADDR}, Canada.</p>

    <h2>2. Accepted payment methods</h2>
    {CARD_MARKS}
    <ul>
      <li>Credit and debit cards: <strong>Visa</strong> and <strong>Mastercard</strong>, through the secure checkout of our payment provider, Wise.</li>
      <li>Bank transfer (details are on the invoice).</li>
    </ul>
    <p>Payments are made against an invoice issued after you accept a written proposal. The invoice includes a secure payment link.</p>

    <h2>3. Currency</h2>
    <p>All prices and transactions are in <strong>Canadian dollars (CAD, $)</strong>. If your card is in another currency, your card issuer converts the amount and may charge a foreign transaction fee.</p>

    <h2>4. Service delivery policy</h2>
    <ul>
      <li>We sell professional services only. <strong>No physical goods are shipped</strong>, so there are no shipping charges.</li>
      <li>Services are delivered remotely by video conference, or on-site at the location agreed in the proposal.</li>
      <li>Training is delivered live online or in-company. Course materials, reports, documents, PMIS configurations and Power BI dashboards are delivered electronically (email, shared folder or your own systems).</li>
      <li>Start dates and timelines are confirmed in the proposal. Typical durations: training courses and workshops ½ to 3 days; PMO diagnostic 2–3 weeks; PMO implementation or improvement 6–12 weeks; PMIS implementation 4–12 weeks; consulting and mentoring monthly.</li>
      <li>There is no special or expedited delivery option, but urgent start dates can be discussed in the proposal.</li>
    </ul>

    <h2>5. Export restrictions</h2>
    <p>Our Services are subject to Canadian export control and sanctions laws, including the <em>Special Economic Measures Act</em> and the <em>Export and Import Permits Act</em>. We do not provide Services to persons, entities or jurisdictions under Canadian sanctions. Our consulting services are not otherwise subject to export restrictions.</p>

    <h2>6. Payment security</h2>
    <ul>
      <li>This website is served only over encrypted HTTPS (TLS).</li>
      <li>Card payments are entered on, and processed by, Wise's PCI DSS-compliant payment page. Card details are transmitted encrypted directly to the payment provider.</li>
      <li>ModernPMO <strong>never receives, sees or stores</strong> your full card number, expiry date or security code.</li>
      <li>We will never ask for card details by email, phone or through our website forms. Payment links are sent only from an <strong>@modernpmo.com</strong> email address. If you receive a suspicious request, contact us before paying.</li>
    </ul>

    <h2>7. Receipts, refunds and cancellations</h2>
    <p>You receive a receipt by email after each payment. Refunds and cancellations follow our <a href="/refund-policy.html">Refund &amp; Cancellation Policy</a>, and all engagements are subject to our <a href="/terms.html">Terms &amp; Conditions</a>.</p>

    <h2>8. Customer service</h2>
    {CONTACT_EN}
    <p>Monday to Friday, 9:00–17:00 Mountain Time. We reply within 1 business day.</p>
"""

PAYMENTS_PT = f"""
    <p>Esta página explica como pagar pelos nossos Serviços, como eles são entregues e como suas informações de pagamento são protegidas. Esta é uma tradução; em caso de divergência, prevalece a <a href="/payments.html">versão em inglês</a>.</p>

    <h2>1. Localização da empresa</h2>
    <p>A {BIZ} é uma empresa <strong>sediada no Canadá</strong>. Nosso endereço comercial permanente é {ADDR}, Canadá.</p>

    <h2>2. Formas de pagamento aceitas</h2>
    {CARD_MARKS}
    <ul>
      <li>Cartões de crédito e débito: <strong>Visa</strong> e <strong>Mastercard</strong>, pelo checkout seguro do nosso provedor de pagamentos, a Wise.</li>
      <li>Transferência bancária (dados na fatura).</li>
    </ul>
    <p>Os pagamentos são feitos contra uma fatura emitida após o aceite de uma proposta por escrito. A fatura inclui um link de pagamento seguro.</p>

    <h2>3. Moeda</h2>
    <p>Todos os preços e transações são em <strong>dólares canadenses (CAD, $)</strong>. Se o seu cartão for em outra moeda, o emissor faz a conversão e pode cobrar tarifa de transação internacional (IOF/taxas, conforme o caso).</p>

    <h2>4. Política de entrega dos serviços</h2>
    <ul>
      <li>Vendemos apenas serviços profissionais. <strong>Nenhum produto físico é enviado</strong>, portanto não há custo de frete.</li>
      <li>Os serviços são prestados remotamente por videoconferência, ou presencialmente no local acordado na proposta.</li>
      <li>Treinamentos são realizados ao vivo online ou in-company. Materiais, relatórios, documentos, configurações de PMIS e dashboards de Power BI são entregues eletronicamente (e-mail, pasta compartilhada ou nos seus próprios sistemas).</li>
      <li>Datas de início e prazos são confirmados na proposta. Durações típicas: treinamentos e workshops de ½ a 3 dias; diagnóstico de PMO 2–3 semanas; implantação ou melhoria de PMO 6–12 semanas; implantação de PMIS 4–12 semanas; consultoria e mentoria mensais.</li>
      <li>Não há opção de entrega especial ou expressa, mas inícios urgentes podem ser discutidos na proposta.</li>
    </ul>

    <h2>5. Restrições de exportação</h2>
    <p>Nossos Serviços estão sujeitos às leis canadenses de controle de exportação e sanções, incluindo o <em>Special Economic Measures Act</em> e o <em>Export and Import Permits Act</em>. Não prestamos Serviços a pessoas, entidades ou jurisdições sob sanções canadenses. Fora isso, nossos serviços de consultoria não estão sujeitos a restrições de exportação.</p>

    <h2>6. Segurança do pagamento</h2>
    <ul>
      <li>Este site é servido somente por HTTPS criptografado (TLS).</li>
      <li>Os dados do cartão são digitados e processados na página de pagamento da Wise, em conformidade com o PCI DSS, e transmitidos de forma criptografada diretamente ao provedor de pagamentos.</li>
      <li>A ModernPMO <strong>nunca recebe, vê ou armazena</strong> o número completo, a validade ou o código de segurança do seu cartão.</li>
      <li>Nunca pedimos dados de cartão por e-mail, telefone ou formulários do site. Links de pagamento são enviados apenas de um endereço <strong>@modernpmo.com</strong>. Se receber uma solicitação suspeita, fale conosco antes de pagar.</li>
    </ul>

    <h2>7. Recibos, reembolsos e cancelamentos</h2>
    <p>Você recebe um recibo por e-mail após cada pagamento. Reembolsos e cancelamentos seguem a nossa <a href="/pt/reembolso.html">Política de Reembolso e Cancelamento</a>, e todos os projetos estão sujeitos aos nossos <a href="/pt/termos.html">Termos e Condições</a>.</p>

    <h2>8. Atendimento ao cliente</h2>
    {CONTACT_PT}
    <p>Segunda a sexta, 9h–17h (horário das Montanhas, Canadá). Respondemos em até 1 dia útil.</p>
"""

THANKS_EN = """
    <p>Thank you! Your service request has been received. We will reply within 1 business day to schedule a free discovery call.</p>
    <p style="margin-top:28px"><a href="/" class="btn btn-primary">Back to home</a></p>
"""
THANKS_PT = """
    <p>Obrigado! Sua solicitação foi recebida. Respondemos em até 1 dia útil para agendar uma conversa inicial gratuita.</p>
    <p style="margin-top:28px"><a href="/pt/" class="btn btn-primary">Voltar ao início</a></p>
"""

PAGES = [
    ("en", "terms.html", "Terms &amp; Conditions", TERMS_EN, "/pt/termos.html", True),
    ("en", "refund-policy.html", "Refund &amp; Cancellation Policy", REFUND_EN, "/pt/reembolso.html", True),
    ("en", "privacy.html", "Privacy Policy", PRIVACY_EN, "/pt/privacidade.html", True),
    ("en", "payments.html", "Payments, Delivery &amp; Security", PAYMENTS_EN, "/pt/pagamentos.html", True),
    ("en", "thanks.html", "Request received", THANKS_EN, "/pt/obrigado.html", False),
    ("pt", "pt/termos.html", "Termos e Condições", TERMS_PT, "/terms.html", True),
    ("pt", "pt/reembolso.html", "Política de Reembolso e Cancelamento", REFUND_PT, "/refund-policy.html", True),
    ("pt", "pt/privacidade.html", "Política de Privacidade", PRIVACY_PT, "/privacy.html", True),
    ("pt", "pt/pagamentos.html", "Pagamentos, Entrega e Segurança", PAYMENTS_PT, "/payments.html", True),
    ("pt", "pt/obrigado.html", "Solicitação recebida", THANKS_PT, "/thanks.html", False),
]

if __name__ == "__main__":
    for lang, path, title, body, other, legal in PAGES:
        with io.open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(lang, path, title, body, other, legal))
        print("wrote", path)
