import { createRouter, createWebHistory } from 'vue-router'
import Sobreviventes from "../views/Sobreviventes.vue";
import Inventarios from "../views/Inventarios.vue";
import Comercio from "../views/Comercio.vue";
import Relatorios from "../views/Relatorios.vue";
import AdicionarSobrevivente from "../views/AdicionarSobrevivente.vue";
import AlterarLocal from "../views/AlterarLocal.vue";

const routes = [
  {
    path: '/',
    name: 'sobreviventes',
    component: Sobreviventes
  },
  {
    path: '/inventarios',
    name: 'inventarios',
    component: Inventarios
  },
  {
    path: '/comercio',
    name: 'comercio',
    component: Comercio
  },
  {
    path: '/relatorios',
    name: 'relatorios',
    component: Relatorios
  },
  {
    path: '/sobreviventes/adicionar',
    name: 'adicionar-sobrevivente',
    component: AdicionarSobrevivente
  },
  {
    path: '/sobreviventes/alterar-local',
    name: 'alterar-local',
    component: AlterarLocal
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
