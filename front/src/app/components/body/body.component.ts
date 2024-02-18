import { Component } from '@angular/core';
import { SearchService } from '../../services/search.service';
import { SerachResult } from '../../interfaces/serach-result';
import { CommonModule } from '@angular/common'; 
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { FormsModule } from '@angular/forms';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-body',
  standalone: true,
  imports: [
    CommonModule,
    PrimeNgModule,
    FormsModule
  ],
  templateUrl: './body.component.html',
  styleUrl: './body.component.css',
  animations: [
    trigger('overlayContentAnimation', [
      state('start', style({ opacity:  0 })),
      state('end', style({ opacity:  1 })),
      transition('start => end', animate('500ms ease-in')),
      transition('end => start', animate('500ms ease-out'))
    ])
  ]
})
export class BodyComponent {
  isLoading = false;
  sources! : string[];

  constructor(private searchService: SearchService, private cd: ChangeDetectorRef) { }
  ngOnInit(): void {
    this.searchService.get_available_authors().then(result => {
      this.sources = result
    })
   }

  query!: string;
  total = 0;
  selectedSource!: string;
  searchResult!: SerachResult | null;

  sourceName(source: string){
    const nameWithoutExtension = source.split('.')[0]; // Quitar la extensión .csv
    const words = nameWithoutExtension.split('_'); // Dividir por '_'
    const formattedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1)); // Capitalizar
    const newFilename = `${formattedWords.join(' ')}`; // Unir y agregar extensión

    console.log(newFilename);
    return newFilename
  }

  search() {
    this.searchResult = null;
    this.isLoading = true;
    console.log('url: ', this.query);
    console.log('source: ', this.selectedSource)
    this.searchService.search(this.query, this.selectedSource, this.total).then(result => {
      this.searchResult = result;
      console.log('base: ', this.searchResult.base)
      this.isLoading = false;
    })
  }

  blockDocument() {
    this.cd.markForCheck();
  }
}
