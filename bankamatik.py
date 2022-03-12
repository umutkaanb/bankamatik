import tkinter
from tkinter import messagebox, Entry
from tkinter import *
import tkinter as tk
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import datetime
import time



pencere = tk.Tk()
yazi=Label(text="ukBank'a Hoş Geldiniz", font="Times 25 italic", bg="black", fg="white")
yazi.pack()
parmak_izi=Label(text="""Bankamatiğe giriş için lütfen aşağıdaki butona parmağınızı okutunuz.\nParmak izinizi okuttuktan sonra kart şifrenizi giriniz""",fg="white", bg="black",anchor=E)
parmak_izi.pack()
resim = tk.PhotoImage(file="../Bankamatik/resmm.png")
width, height = resim.width(), resim.height()
canvas = tk.Canvas(pencere, width=width, height=height)
canvas.pack()






def parmak_izi_fonk():
    tts = gTTS(text='Parmak iziniz okundu, lütfen kart şifrenizi giriniz.', lang='tr')
    tts.save("parmak_izi.mp3")
    os.system("parmak_izi.mp3")
    p_izi_btn.destroy()
    frame=Frame(pencere)
    frame.pack()

    def girisYap():
        sifre = "1234"
        parola=kullanici.get()
        if parola == sifre:
            tts = gTTS(text='Şifreniz doğru, lütfen yapmak istediğiniz işlemi söyleyiniz.', lang='tr')
            tts.save("doğru_şifre.mp3")
            os.system("doğru_şifre.mp3")
            giris_btn.destroy()
            kullanici.destroy()
            yazi.destroy()
            parmak_izi.destroy()

            def k_bilgiler_gosterme():
                k_bilgiler_pencere = tk.Tk()
                bilgiler = Label(k_bilgiler_pencere,text="Kart Bilgileriniz: ", font="Oswald 20 ", bg="black", fg="white")
                bilgiler.pack()
                bilgiler.place()
                cerceve=Frame()
                cerceve.pack()
                cerceve.place(x=287, y=270)
                with open("para.txt", "r") as dosya:
                    para = int(dosya.readlines()[0])
                k_bilgiler = Label(k_bilgiler_pencere,text="Adı Soyadı: Umut Kaan Boğan\nIBAN: TR 444513513138463515313\nKart Numarası: 4878 8448 8787 7878\nBakiye Miktarı: {}".format(para), bg="white",)
                k_bilgiler.pack()
                k_bilgiler.place()
                k_bilgiler_pencere.resizable(width=False, height=False)
                k_bilgiler_pencere.geometry("300x200+1000+250")
                k_bilgiler_pencere.configure(bg="black")
                k_bilgiler_pencere.title("ukBank - Hesap Bilgileri")
                k_bilgiler_pencere.mainloop()

            def p_cekme():
                p_cekme_pencere=tk.Tk()
                p_miktar=Label(p_cekme_pencere,text="Çekmek istediğiniz miktarı aşağıdaki alana giriniz",font="Oswald 20", bg="black", fg="white")
                p_miktar.pack()
                p_miktar.place(x=135, y=270)
                p_giris = Entry(p_cekme_pencere)

                p_giris.pack()
                p_giris.place(x=315, y=340)
                def p_cekme1():
                    para_miktari = Label(p_cekme_pencere,text="Çekilen para miktarı {} TL".format(int(p_giris.get())),font="Oswald 20", bg="black", fg="white")
                    para_miktari.pack()
                    para_miktari.place(x=240, y=430)

                    zaman = datetime.datetime.now()




                    para_miktari.after(1500, para_miktari.destroy)
                    p_cekme_pencere.after(1600, p_cekme_pencere.destroy)

                    with open("para.txt", "r") as dosya:
                        para = int(dosya.readlines()[0])
                    if int(p_giris.get()) <= para:
                        para = para - int(p_giris.get())
                        with open("para.txt", "w") as dosya:
                            dosya.write(str(para))
                        with open("hesap hareketleri.txt","a+") as dosya:
                            dosya.write("{}.{}.{} tarihinde, {}:{} saatinde bankadan çekilen para miktarı {} TL\n".format(zaman.day,zaman.month,zaman.year,zaman.hour,zaman.minute,p_giris.get()))


                    else:
                        tts = gTTS(text='Yetersiz Bakiye, Bakiye Miktarınız {} Türk Lirası'.format(para), lang='tr')
                        tts.save("yetersiz_bakiye.mp3")
                        os.system("yetersiz_bakiye.mp3")





                p_cek = Button(p_cekme_pencere,text="Para Çek", font="Arial 15 italic bold", bg="white", cursor="hand2",command=p_cekme1)
                p_cek.place()
                p_cek.place(x=327, y=375)

                p_cekme_pencere.resizable(width=False, height=False)
                p_cekme_pencere.geometry("750x750+770+0")
                p_cekme_pencere.configure(bg="black")
                p_cekme_pencere.title("ukBank - Para Çekme")
                p_cekme_pencere.mainloop()


            def p_yatirma():
                p_yatirma_pencere = tk.Tk()
                p_miktar = Label(p_yatirma_pencere,text="Yatırmak istediğiniz miktarı aşağıdaki alana giriniz", font="Oswald 20",
                                 bg="black", fg="white")
                p_miktar.pack()
                p_miktar.place(x=135, y=270)
                p_giris = Entry(p_yatirma_pencere)
                p_giris.pack()
                p_giris.place(x=315, y=340)


                def p_yatirma1():
                    para_miktari = Label(p_yatirma_pencere,text="Yatırılan para miktarı {} TL".format(int(p_giris.get())), font="Oswald 20",
                                         bg="black", fg="white")
                    para_miktari.after(1800, para_miktari.destroy)
                    para_miktari.pack()
                    para_miktari.place(x=240, y=430)

                    with open("para.txt", "r") as dosya:
                        para = int(dosya.readlines()[0])

                    para=para+int(p_giris.get())
                    with open("para.txt", "w") as dosya:
                        dosya.write(str(para))

                    with open("hesap hareketleri.txt", "a+") as dosya:
                        zaman = datetime.datetime.now()
                        dosya.write(
                            "{}.{}.{} tarihinde, {}:{} saatinde bankaya yatırılan para miktarı {} TL\n".format(zaman.day,
                                                                                                              zaman.month,
                                                                                                              zaman.year,
                                                                                                              zaman.hour,
                                                                                                              zaman.minute,
                                                                                                              p_giris.get()))

                    p_yatirma_pencere.after(2000, p_yatirma_pencere.destroy)

                p_yatir = Button(p_yatirma_pencere,text="Para Yatır", font="Arial 15 italic bold", bg="white", cursor="hand2",
                               command=p_yatirma1)
                p_yatir.place()
                p_yatir.place(x=320, y=375)

                p_yatirma_pencere.resizable(width=False, height=False)
                p_yatirma_pencere.geometry("750x750+770+0")
                p_yatirma_pencere.configure(bg="black")
                p_yatirma_pencere.title("ukBank - Para Yatırma")
                p_yatirma_pencere.mainloop()


            def k_iade():
                messagebox.showinfo("İade", "Kartınızı iade alabilirsiniz, iyi günler.")
                pencere.destroy()

            def havale():
                havale_pencere = tk.Tk()
                h_iban = Label(havale_pencere,text="     Havale yapmak istediğiniz IBAN numarası:", font="Oswald 20",
                                 bg="black", fg="white")
                h_iban.pack()
                h_iban.place(x=135, y=270)
                h_giris = Entry(havale_pencere)
                h_giris.pack()
                h_giris.place(x=315, y=340)
                def devam():
                    def h_gonder():
                        with open("para.txt", "r") as dosya:
                            para = int(dosya.readlines()[0])
                        if int(h_pgiris.get()) <= para:
                            para = para - int(h_pgiris.get())
                            with open("para.txt", "w") as dosya:
                                dosya.write(str(para))

                        else:
                            tts = gTTS(text='Yetersiz Bakiye, Bakiye Miktarınız {} Türk Lirası'.format(para), lang='tr')
                            tts.save("yetersiz_bakiye.mp3")
                            os.system("yetersiz_bakiye.mp3")








                        h_para.destroy()
                        h_pgiris.destroy()
                        h_gonder.destroy()
                        basarili_islem = Label(havale_pencere,
                                               text="İşlem başarılı, 3 saniye sonra pencere kapanacaktır.",
                                               font="Oswald 18",
                                               bg="black", fg="white")
                        basarili_islem.pack()
                        basarili_islem.place(x=140, y=375)
                        havale_pencere.after(3000, havale_pencere.destroy)



                    h_buton.destroy()
                    h_iban.destroy()
                    h_giris.destroy()
                    h_para = Label(havale_pencere,text="     Havale yapmak istediğiniz para miktarı:", font="Oswald 20",
                                 bg="black", fg="white")
                    h_para.pack()
                    h_para.place(x=135, y=270)
                    h_pgiris = Entry(havale_pencere)
                    h_pgiris.pack()
                    h_pgiris.place(x=315, y=340)
                    h_gonder = Button(havale_pencere, text="Devam", font="Times 11 bold", cursor="hand2", height=1,command=h_gonder)
                    h_gonder.pack()
                    h_gonder.place(x=347, y=372)


                h_buton = Button(havale_pencere, text="Devam", font="Times 11 bold", cursor="hand2", height=1,
                                   command=devam)
                h_buton.pack()
                h_buton.place(x=347, y=372)





                havale_pencere.resizable(width=False, height=False)
                havale_pencere.geometry("750x750+770+0")
                havale_pencere.configure(bg="black")
                havale_pencere.title("ukBank - Havale")
                havale_pencere.mainloop()


            def h_hareketler():
                pencere1 = tk.Tk()
                pencere1.title("ukBank - Hesap Hareketleri")
                pencere1.geometry("400x350+1000+250")
                pencere1.resizable(width=False, height=False)

                with open("hesap hareketleri.txt", "r") as dosya:
                    h_hareketleri = dosya.readlines()[0:10]


                hareketler = Label(pencere1,text=h_hareketleri)
                hareketler.pack()
                hareketler.place(x=1,y=1)





            islemler=Label(text="Yapmak İstediğiniz İşlemi Seçiniz", font="Oswald 20", bg="black", fg="white")
            islemler.pack()
            islemler.place(x=25, y=130)


            k_bilgiler_btn = Button(text="Kart Bilgileri", font="Arial 15 italic bold", bg="white", cursor="hand2",command=k_bilgiler_gosterme)
            k_bilgiler_btn.pack()
            k_bilgiler_btn.place(x=25, y=195)

            p_cekme_btn = Button(text="Para Çekme", font="Arial 15 italic bold", bg="white", cursor="hand2",command=p_cekme)
            p_cekme_btn.pack()
            p_cekme_btn.place(x=25, y=250)

            p_yatirma_btn = Button(text="Para Yatırma", font="Arial 15 italic bold", bg="white", cursor="hand2", command=p_yatirma)
            p_yatirma_btn.pack()
            p_yatirma_btn.place(x=25, y=305)

            havale_btn = Button(text="Havale", font="Arial 15 italic bold", bg="white", cursor="hand2",command = havale)
            havale_btn.pack()
            havale_btn.place(x=650, y=195)

            h_hareketler_btn = Button(text="Hesap Hareketleri", font="Arial 15 italic bold", bg="white", cursor="hand2",command=h_hareketler)
            h_hareketler_btn.pack()
            h_hareketler_btn.place(x=544, y=250)


            k_iade_btn = Button(text="Kart İade", font="Arial 15 italic bold", bg="white", cursor="hand2",command=k_iade)
            k_iade_btn.pack()
            k_iade_btn.place(x=626, y=305)



        else:
            uyari2=messagebox.showwarning("Hata", "Yanlış şifre, sistem kapatılıyor!")
            tts = gTTS(text='Yanlış şifre, sistem kapatılıyor.', lang='tr')
            tts.save("yanlış_şifre.mp3")
            os.system("yanlış_şifre.mp3")
            pencere.destroy()

    giris_btn = Button(pencere, text="Giriş Yap", font="Times 11 bold", cursor="hand2", height=1, command=girisYap)
    giris_btn.pack()
    giris_btn.place(x=341, y=450)

    kullanici = Entry(pencere)
    kullanici.pack()
    kullanici.place(x=313, y=420)

p_izi_btn=Button(text="Parmak İzi", font="Times 11 bold", cursor="hand2", command=parmak_izi_fonk)
p_izi_btn.pack()
p_izi_btn.place(x=334, y=415)






canvas.create_image((380, 345), image=resim)
entry = tk.Entry(master=canvas)







pencere.resizable(width=False, height=False)
pencere.geometry("750x750+0+0")
pencere.configure(bg="black")
pencere.title("ukBank")
pencere.mainloop()
