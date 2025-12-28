import { NgModule, provideBrowserGlobalErrorListeners } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { App } from './app';
import { appRoutes } from './app.routes';
import { NxWelcome } from './nx-welcome';
import { UiModule } from '@workspace/ui';

@NgModule({
  declarations: [App, NxWelcome],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    UiModule, // Shared UI components library
  ],
  providers: [provideBrowserGlobalErrorListeners()],
  bootstrap: [App],
})
export class AppModule {}
