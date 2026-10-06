# Gemi Ana Boyutları ve Form Katsayıları Hesaplayıcı

def gemi_hesapla(lbp: float, b: float, t: float, cb: float):
    # Deniz suyu yoğunluğu (t/m^3)
    rho = 1.025  

    # Deplasman hacmi: ∇ = L * B * T * Cb
    nabla = lbp * b * t * cb

    # Deplasman ağırlığı: Δ = ∇ * ρ
    deplasman = nabla * rho

    print("-" * 40)
    print("      GEMİ HİDROSTATİK ÖZETİ")
    print("-" * 40)
    print(f"Kaimeler Arası Boy (Lbp) : {lbp:.2f} m")
    print(f"Kalıp Genişliği (B)      : {b:.2f} m")
    print(f"Su Çekimi (T)            : {t:.2f} m")
    print(f"Blok Katsayısı (Cb)      : {cb:.3f}")
    print("-" * 40)
    print(f"Deplasman Hacmi (∇)      : {nabla:.2f} m³")
    print(f"Deplasman Ağırlığı (Δ)   : {deplasman:.2f} ton")
    print("-" * 40)

if __name__ == "__main__":
    print("Gemi Bilgilerini Giriniz:")
    L = float(input("Lbp (m): "))
    B = float(input("Genişlik (m): "))
    T = float(input("Draft (m): "))
    Cb = float(input("Blok Katsayısı (örn: 0.65): "))

    gemi_hesapla(L, B, T, Cb)