def caesar(original_text, shift_amount, encode_or_decode):
    alfabe="abcdefghijklmnopqrstuvwxyz"
    output_text=""
    if encode_or_decode=="2":
        shift_amount*=-1
        encode_or_decode="decode"
    else:
        encode_or_decode="encode"

    for harf in original_text:
        if harf in alfabe:
            shifted_position=(alfabe.index(harf) + shift_amount)
            shifted_position%=len(alfabe)
            output_text+=alfabe[shifted_position]
        else:
            output_text+=harf
    print(f"Here is the {encode_or_decode}d result: {output_text}")

tamam_mı_devam_mı=True

while tamam_mı_devam_mı:

    direction=input("Yapmak İstediğiniz İşlemi Seçin (1-Encode, 2-Decode): ")
    text=input("Mesajı Giriniz: ").lower()
    shift=int(input("Kaydırma Numarasını Giriniz: "))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    devam=input("Tekrar İşlem Yapmak İstiyor Musunuz (e/h) ? : ").lower()
    if devam==("h"):
        print(".....")
        tamam_mı_devam_mı=False

