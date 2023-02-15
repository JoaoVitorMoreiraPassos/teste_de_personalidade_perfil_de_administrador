from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt
import numpy as np
import hashlib
import os
from .models import Imagem
from time import time

# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def index(request):
    if request.method == "POST":
        t1 = time()
        ip = get_client_ip(request)
        print(ip)
        ip = hashlib.md5(ip.encode()).hexdigest()
        print(ip)
        headers = None
        values = dict(request.POST)
        values = values['resposta']
        values = list(map(lambda x: 1 if x == "" else int(x), values))
        with (open("utils/home/headers.txt", "r")) as file:
            file = file.read()
            file = file.split("\n")
            headers = file
        headers = list(map(lambda x: x+".", headers))
        groups = [
            [0, 10, 20],
            [9, 19, 21],
            [8, 18, 22],
            [7, 17, 23],
            [6, 16, 24],
            [5, 15, 25],
            [4, 14, 26],
            [3, 13, 27],
            [2, 12, 28],
            [1, 11, 29]
        ]
        temp = []
        for i in groups:
            temp.append(sum([values[i[0]], values[i[1]], values[i[2]]]))
        values = temp
        values.append(values[0])
        headers_len = len(headers)
        angulos = [n / float(headers_len) * 2 *
                   np.pi for n in range(headers_len)]
        angulos += angulos[:1]

        # Crie o gráfico de radar decagonal:
        fig = plt.figure(figsize=(18, 18))
        ax = fig.add_subplot(111, polar=True)

        # Adicione as linhas do gráfico:
        ax.plot(angulos, values, marker="*")
        ax.fill(angulos, values, 'teal', alpha=1)

        ax.set_ylim([0, 15])  # Fixando o limite do eixo radial em 15
        ax.set_rgrids(range(0, 16, 1), fontsize=16)
        ax.set_thetagrids([a * 360 / 16 for a in range(10)],
                          labels=headers,
                          fontsize=20)

        # Adicione as headers como rótulos:
        ax.set_xticks(angulos[:-1])
        ax.set_xticklabels(headers, y=0.1, fontsize=15)

        # Adicione uma legenda:
        # ax.set_title("Seu Resultado", fontsize=20, y=1.1)
        try:
            os.system("mkdir media/home/" + ip)
        except Exception:
            pass
        plt.savefig(f"media/home/{ip}/img.png")

        img = Imagem.objects.filter(name=ip)
        if len(img) > 0:
            Imagem.delete(img[0])
        img = Imagem()
        img.name = ip
        img.image = f"media/home/{ip}/img.png"
        img.save()
        print(time() - t1)
        return render(request, 'home/index.html', context={
            'labels': ['test'],
            'have_image': True,
            'img': img
        })

    quests = None
    with open('utils/home/quests.txt', 'r') as f:
        quests = f.readlines()
    return render(request, 'home/index.html', context={
        'labels': quests,
        'have_image': False,
        'img_url': None
    })
