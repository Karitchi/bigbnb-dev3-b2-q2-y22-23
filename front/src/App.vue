<template>
  <div>
    <header class="navbar navbar-expand-lg my-header">
      <a class="navbar-brand" href="#">Logo ici</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Se connecter</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">S'inscrire</a>
          </li>
        </ul>
      </div>
    </header>
    <router-view/>
    <!-- Contenu de la page ici -->
    <section>
      <div >
        <h2>Test titre</h2>
        <p>Test simple texte</p>
      </div>
    </section>

    <footer class="my-footer py-3">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-center">
            <a href="#" class="mx-2">big_bnb.inc</a>|
            <router-link to="/login" class="mx-2">Confidentialité</router-link>|
            <a href="#" class="mx-2">Conditions générales</a>|
            <a href="#" class="mx-2">Plan du site</a>|
            <a href="#" class="mx-2">Infos de l'entreprise</a>|
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>


<style lang="scss">
  @import './assets/variables.scss';
</style>
