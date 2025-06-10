import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, {
  ...appConfig,
  providers: [
    ...(appConfig.providers ?? []),   // conserve les providers actuels s’il y en a
    importProvidersFrom(HttpClientModule),  // ajoute HttpClientModule ici
  ]
})  .catch((err) => console.error(err));
