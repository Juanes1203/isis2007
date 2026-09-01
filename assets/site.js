/* ==========================================================================
   ISIS2007 — Cabecera y pie de página compartidos.
   Se inyectan por JS para que todas las páginas mantengan la misma
   navegación sin duplicar markup.
   ========================================================================== */
(function () {
  'use strict';

  var NAV = [
    { href: 'index.html', label: 'Inicio' },
    { href: 'schedule.html', label: 'Cronograma' },
    { href: 'actividades.html', label: 'Actividades' },
    { href: 'recursos-materiales.html', label: 'Recursos' },
    { href: 'claude-101.html', label: 'Claude 101' },
    { href: 'team.html', label: 'Equipo' }
    /* Secciones desactivadas — para reactivarlas, descomenta la línea
       correspondiente y bórrala de DISABLED (abajo):
    , { href: 'ruleta-estudiantes.html', label: 'Ruleta' }
    , { href: 'asistencia-simple.html', label: 'Asistencia' }
    */
  ];

  /* Páginas fuera de servicio: se muestra un aviso en lugar del contenido,
     de modo que tampoco queden accesibles por enlace directo. */
  var DISABLED = {
    'ruleta-estudiantes.html': 'Ruleta de estudiantes',
    'asistencia-simple.html': 'Registro de asistencia'
  };

  /* Páginas que deben marcar como activo otro enlace del menú */
  var ALIASES = {
    'asistencia.html': 'asistencia-simple.html',
    'working-attendance.html': 'asistencia-simple.html',
    'simple-attendance.html': 'asistencia-simple.html',
    'acceso-archivos.html': 'recursos-materiales.html',
    'claude-101-laboratorio.html': 'claude-101.html',
    'claude-101-prompts.html': 'claude-101.html',
    'claude-101-practicas.html': 'claude-101.html',
    'claude-101-cheatsheet.html': 'claude-101.html',
    'claude-101-recursos.html': 'claude-101.html',
    'claude-101-herramientas.html': 'claude-101.html',
    '': 'index.html'
  };

  var SEMESTER = '2026-II';
  var ROOM = 'S1_202';
  var TIME = '11:00 a. m. – 1:50 p. m.';

  function currentPage() {
    var file = window.location.pathname.split('/').pop().toLowerCase();
    return ALIASES[file] || file;
  }

  function buildTopbar(active) {
    var links = NAV.map(function (item) {
      var cls = item.href === active ? ' class="is-active"' : '';
      return '<a href="' + item.href + '"' + cls + '>' + item.label + '</a>';
    }).join('');

    var el = document.createElement('header');
    el.className = 'topbar';
    el.innerHTML =
      '<div class="topbar__inner">' +
        '<a href="index.html" class="brand">' +
          '<span class="brand__mark">IS</span>' +
          '<span class="brand__text">' +
            '<span class="brand__code">ISIS2007</span>' +
            '<span class="brand__sub">Uniandes · ' + SEMESTER + '</span>' +
          '</span>' +
        '</a>' +
        '<nav class="mainnav" id="mainnav">' + links + '</nav>' +
        '<button class="navtoggle" type="button" aria-label="Abrir menú" ' +
          'aria-expanded="false" aria-controls="mainnav">' +
          '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">' +
            '<path d="M1 4h16M1 9h16M1 14h16" stroke="currentColor" ' +
              'stroke-width="1.7" stroke-linecap="round" fill="none"/>' +
          '</svg>' +
        '</button>' +
      '</div>';
    return el;
  }

  function buildFooter() {
    var links = NAV.slice(1).map(function (item) {
      return '<a href="' + item.href + '">' + item.label + '</a>';
    }).join('');

    var el = document.createElement('footer');
    el.className = 'sitefooter';
    el.innerHTML =
      '<div class="sitefooter__inner">' +
        '<div>' +
          '<div class="sitefooter__brand">' +
            '<span class="sitefooter__bar"></span>' +
            '<strong>Universidad de los Andes</strong>' +
          '</div>' +
          'Departamento de Ingeniería de Sistemas y Computación<br>' +
          'ISIS2007 · Diseño de Productos e Innovación en TI' +
        '</div>' +
        '<div>' +
          '<strong>Navegación</strong>' +
          '<div class="sitefooter__links mt-16">' + links + '</div>' +
        '</div>' +
        '<div>' +
          '<strong>Semestre ' + SEMESTER + '</strong><br>' +
          'Clases: miércoles · ' + TIME + '<br>' +
          'Salón ' + ROOM + '<br>' +
          'Bogotá, Colombia' +
        '</div>' +
      '</div>' +
      '<div class="sitefooter__meta">' +
        'Portal del curso · uso académico. Contenido administrado por el equipo docente.' +
      '</div>';
    return el;
  }

  function buildDisabledNotice(title) {
    var el = document.createElement('section');
    el.className = 'page-off';
    el.innerHTML =
      '<div class="wrap wrap--narrow">' +
        '<div class="page-off__box">' +
          '<span class="eyebrow">Sección no disponible</span>' +
          '<h1>' + title + '</h1>' +
          '<p>' +
            'Esta herramienta está temporalmente fuera de servicio. ' +
            'Si necesitas algo relacionado, escribe al equipo docente.' +
          '</p>' +
          '<div class="btnrow">' +
            '<a href="index.html" class="btn">Volver al inicio</a>' +
            '<a href="team.html" class="btn btn--ghost">Contactar al equipo docente</a>' +
          '</div>' +
        '</div>' +
      '</div>';
    return el;
  }

  function mount() {
    var active = currentPage();

    if (!document.querySelector('.topbar')) {
      document.body.insertBefore(buildTopbar(active), document.body.firstChild);
    }

    /* Si la página está desactivada, se oculta su contenido y se deja el aviso.
       El DOM original se conserva para que los scripts de la página no fallen. */
    if (DISABLED[active]) {
      var page = document.querySelector('.page') || document.body;
      document.body.classList.add('is-page-off');
      page.insertBefore(buildDisabledNotice(DISABLED[active]), page.firstChild);
    }

    if (!document.querySelector('.sitefooter') && !document.body.hasAttribute('data-no-footer')) {
      document.body.appendChild(buildFooter());
    }

    var toggle = document.querySelector('.navtoggle');
    var nav = document.getElementById('mainnav');
    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', String(open));
      });
      nav.addEventListener('click', function (e) {
        if (e.target.tagName === 'A') nav.classList.remove('is-open');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
