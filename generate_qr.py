"""
Script officiel pour générer le QR Code de la conférence EMSI - CFC Casablanca
Thème Option B : Royal Morocco (Bleu nuit #080e1e, Or #d4af37) avec Logo EMSI officiel au centre
"""
import os
import qrcode
from PIL import Image, ImageDraw

def generate_styled_qr(url="https://geoconferenceemsi-del.github.io/geo-conference/", output_path="qr-conference.png", logo_path="emsi_logo.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Couleurs Royal Morocco
    img = qr.make_image(fill_color="#080e1e", back_color="#ffffff").convert("RGBA")
    qr_w, qr_h = img.size

    # Intégration du Logo EMSI au centre si disponible
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo_w = int(qr_w * 0.28)
        aspect = logo.height / logo.width
        logo_h = int(logo_w * aspect)
        logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

        pad = 8
        badge_w = logo_w + pad * 2
        badge_h = logo_h + pad * 2
        pos_x = (qr_w - badge_w) // 2
        pos_y = (qr_h - badge_h) // 2

        badge = Image.new("RGBA", (badge_w, badge_h), (255, 255, 255, 255))
        draw = ImageDraw.Draw(badge)
        draw.rectangle([0, 0, badge_w - 1, badge_h - 1], outline="#d4af37", width=2)

        img.paste(badge, (pos_x, pos_y))
        img.paste(logo, (pos_x + pad, pos_y + pad), logo)

    # Cadre extérieur doré
    border_w = 8
    total_w = qr_w + border_w * 2
    total_h = qr_h + border_w * 2
    final_img = Image.new("RGBA", (total_w, total_h), "#ffffff")
    final_img.paste(img, (border_w, border_w))

    final_draw = ImageDraw.Draw(final_img)
    for i in range(3):
        final_draw.rectangle([i, i, total_w - 1 - i, total_h - 1 - i], outline="#d4af37")

    final_img.save(output_path)
    print(f"[OK] QR Code officiel généré avec succès -> {output_path} (URL: {url})")

if __name__ == "__main__":
    generate_styled_qr()
