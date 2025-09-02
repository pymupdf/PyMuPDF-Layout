where
$$
X = \begin{pmatrix}
l_a - 302.1 \\
R - 1.71 \\
z_* - 1090.04
\end{pmatrix} \quad (23)
$$
and the inverse covariance matrix
$$
C_M^{-1} = \begin{pmatrix}
1.8 & 27.968 & -1.103 \\
27.968 & 5667.577 & -92.263 \\
-1.103 & -92.263 & 2.923
\end{pmatrix} \quad (24)
$$
The fourth set of observational data is 12 Hubble evolution data from [21] and [22], its $\chi^2_H$ is defined as
$$
\chi^2_H = \sum_{i=1}^{12} \frac{[H(z_i) - H_{ob}(z_i)]^2}{\sigma^2_i} \quad (25)
$$
Note that redshifts of these data fall in the region $z \in (0,1.75)$.
In summary,
$$
\chi^2_{\text{total}} = \tilde{\chi}^2_{\text{sn}} + \chi^2_{\text{cmb}} + \chi^2_{\text{bao}} + \chi^2_H \quad (26)
$$

## IV. FITTING RESULTS

### A. Model I

At first, we divide the whole region of redshift into 4 bins (i.e., $m=3$), the divided points and boundaries are $(0, z_1, z_2, 1.8, \infty)$, where $z_1$ and $z_2$ are left as free parameters of the model, and $0 < z_1 < z_2 < 1.8$. In the fourth bin we set $w_L = -1$. It means that we divide the region with $z \in (0,1.8)$ into 3 bins and seek for two possible turning points of $w_{\text{de}}(z)$ in this region. The reconstructed $w_{\text{de}}$ of the best-fitted model is shown in Fig. 1,

| Models | $\tilde{\chi}^2_{\text{sn,min}}$ | $\chi^2_{\text{cmb,min}}$ | $\chi^2_{\text{bao,min}}$ | $\chi^2_{H,\text{min}}$ | $\chi^2_{\text{total,min}}$ |
|:-------|:---------------------|:-------------------|:-------------------|:------------------|:--------------------|
| Model I | 459.728              | 0.204              | 1.494              | 5.983             | 467.409             |
| CPL    | 465.621              | 0.251              | 1.716              | 10.818            | 478.406             |
| ACDM   | 465.759              | 1.014              | 1.470              | 10.850            | 479.093             |

TABLE I: The best-fitted $\chi^2$ of four data sets for Model I, CPL model and the ACDM model.