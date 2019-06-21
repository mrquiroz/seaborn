import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def genera(df):
    columnas = df.columns
    columnas = list(columnas)
    columnas.remove('cname')
    columnas.remove('ccodealp')
    columnas.remove('ht_region')
    fu = lambda x: np.mean(df[x])
    analisis = list(map(fu,columnas))
    analisis = {columnas[i]:analisis[i] for i in range(len(columnas))}
    return analisis



def count_nan(df,var,print_list=False): 
    serie = df[var]
    cantidad = 0
    for i in serie:
        if i == 'Nan':   # Lo anterior por que en el sample csv los Nan eran string
            cantidad += 1
        elif type(i) == np.float:
            if np.isnan(i):
                cantidad +=1
    porcentaje = cantidad/len(serie)
    if (print_list):
        index_registro = []
        for i,j in serie.items():
            if type(j) == np.float or j == 'Nan':
                if j == 'Nan':
                    index_registro.append(i)
                elif np.isnan(j):
                    index_registro.append(i)
        return cantidad,porcentaje,index_registro
    return cantidad,porcentaje

def histograma(df,var,true_mean=False,sample_mean=False):
    
    plt.hist(df[var])
    bottom, top = plt.ylim()  # return the current ylim
    plt.ylim((bottom, top))   # set the ylim to bottom, top
    plt.ylim(bottom, top)
    if sample_mean:
        plt.axvline(df[var].mean(), color='k', linestyle='dashed', linewidth=1)
        plt.text(df[var].mean() + df[var].mean()/10, top-top/10, 'Mean: {:.2f}'.format(df[var].mean()))
    if true_mean:
        plt.axvline(df_o[var].mean(), color='r', linestyle='dashed', linewidth=1)
        plt.text(np.mean(df_o[var]) + np.mean(df_o[var])/10, top-top/5, 'True Mean: {:.2f}'.format(np.mean(df_o[var])),bbox=dict(facecolor='red', alpha=0.5))
    plt.show

def count_nan_df(base):
    columnas = base.columns
    fu = lambda x: count_nan(df= base,var =x)
    analisis = {columnas[i]:list(map(fu,columnas))[i] for i in range(len(columnas))}
    analisis = pd.DataFrame.from_dict(analisis)
    analisis.rename(index={0:'cantidad Nan',1:'porcentaje Nan'})
    return analisis


def gen_curvas(df1,df2,variable,log = False):
    if log:
        v1 = np.log(df1[variable])
        v2 = np.log(df2[variable])
        mu = v1.mean()
        sigma = v1.std()
        mu2 = v2.mean()
        sigma2 = v2.std()
        num_bins = 50
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(v1, num_bins, normed=1)
        n2, bins, patchess = ax.hist(v2, num_bins, normed=1)
        y = mlab.normpdf(bins, mu, sigma)
        y2 = mlab.normpdf(bins, mu2, sigma2)
        ax.plot(bins, y,'--',label='df1')
        ax.plot(bins, y2,'--',label='df2')
        ax.legend()
        fig.tight_layout()
        plt.show()
    else:
        v1 = df1[variable]
        v2 = df2[variable]
        mu = v1.mean()
        sigma = v1.std()
        mu2 = v2.mean()
        sigma2 = v2.std()
        num_bins = 50
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(v1, num_bins, normed=1)
        n2, bins, patchess = ax.hist(v2, num_bins, normed=1)
        y = mlab.normpdf(bins, mu, sigma)
        y2 = mlab.normpdf(bins, mu2, sigma2)
        ax.plot(bins, y,'--',label='df1')
        ax.plot(bins, y2,'--',label='df2')
        ax.legend()
        fig.tight_layout()
        plt.show()
