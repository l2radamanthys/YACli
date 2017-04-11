import { Pipe, PipeTransform } from '@angular/core';


@Pipe({
    name: '%selector%'
})
export class %classname% implements PipeTransform {
    transform(value: any, args?: any) {
        return value;
    }
}
