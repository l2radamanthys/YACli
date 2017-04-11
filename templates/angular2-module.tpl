import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { %component% } from './%componentfile%';

@NgModule({
    imports: [
        CommonModule,
    ],
    declarations: [
        %component%,
    ],
    exports:[],
    providers: [],
})
export class %classname% {}

