import { createRouter, createWebHistory } from 'vue-router';
import Sobreviventes from "../views/sobreviventes/Sobreviventes.vue";
import Inventarios from "../views/inventarios/Inventarios.vue";
import Comercio from "../views/comercio/Comercio.vue";
import Relatorios from "../views/relatorios/Relatorios.vue";
import AdicionarSobrevivente from "../views/adicionarsobrevivente/AdicionarSobrevivente.vue";
import AlterarLocal from "../views/alterarlocal/AlterarLocal.vue";

const routes = [
  {
    path: '/',
    name: 'sobreviventes',
    component: Sobreviventes
  },
  {
    path: '/inventarios/',
    name: 'inventarios',
    component: Inventarios
  },
  {
    path: '/comercio/',
    name: 'comercio',
    component: Comercio
  },
  {
    path: '/relatorios/',
    name: 'relatorios',
    component: Relatorios
  },
  {
    path: '/sobreviventes/adicionar/',
    name: 'adicionar-sobrevivente',
    component: AdicionarSobrevivente
  },
  {
    path: '/sobreviventes/alterar-local/',
    name: 'alterar-local',
    component: AlterarLocal
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
