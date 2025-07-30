<script setup lang="ts">
import GitHubSvg from '../../assets/icons/github-svgrepo-com.svg'
import TwitterSvg from '../../assets/icons/icons8-x.svg'
</script>

<template>
  <section class="my-12 sm:my-16 lg:my-20 flex flex-col items-center px-4 sm:px-8 md:px-16 lg:px-20 xl:px-24">
    <!-- Section Title -->
    <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-center mb-6 sm:mb-8 pb-2">
      Author
    </h2>
    
    <!-- Author Card -->
    <div class="bg-gray-50 border border-gray-200 w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl xl:w-1/3 rounded-lg p-4 sm:p-6 lg:p-8 text-center hover:transform hover:-translate-y-1 hover:shadow-lg transition-all duration-200 group">
      <!-- Avatar -->
      <div class="flex justify-center mb-3 sm:mb-4">
        <img 
          src="https://avatars.githubusercontent.com/u/71281020?v=4" 
          class="h-16 w-16 sm:h-20 sm:w-20 lg:h-24 lg:w-24 rounded-full border-2 border-gray-200 group-hover:border-blue-300 transition-colors duration-200 shadow-sm"
          alt="Artur's avatar"
        />
      </div>
      
      <!-- Name -->
      <div class="text-lg sm:text-xl lg:text-2xl font-semibold text-gray-900 mb-1">
        Artur
      </div>
      
      <!-- Role -->
      <div class="text-blue-600 font-medium mb-2 sm:mb-3 text-sm sm:text-base">
        Web enthusiast
      </div>
      
      <!-- Bio -->
      <div class="text-gray-600 text-xs sm:text-sm lg:text-base leading-relaxed mb-3 sm:mb-4 px-2 sm:px-4">
        Web enthusiast and ambassador of Tech who enjoys gachimuchi community.
      </div>
      
      <!-- Social Links -->
      <div class="flex justify-center gap-3 sm:gap-4">
        <a 
          href="https://github.com/Artur0412-KU" 
          target="_blank"
          rel="noopener noreferrer"
          class="p-2 rounded-full bg-white border border-gray-300 hover:border-gray-400 hover:shadow-md transition-all duration-200 group/link"
          aria-label="Visit Artur's GitHub profile"
        >
          <img :src="GitHubSvg" class="h-5 w-5 sm:h-6 sm:w-6 lg:h-7 lg:w-7 group-hover/link:scale-110 transition-transform duration-200" alt="GitHub" />
        </a>
        <a 
          href="https://x.com/04_arti" 
          target="_blank" 
          rel="noopener noreferrer"
          class="p-2 rounded-full bg-white border border-gray-300 hover:border-gray-400 hover:shadow-md transition-all duration-200 group/link"
          aria-label="Visit Artur's Twitter profile"
        >
          <img :src="TwitterSvg" class="h-5 w-5 sm:h-6 sm:w-6 lg:h-7 lg:w-7 group-hover/link:scale-110 transition-transform duration-200" alt="Twitter" />
        </a>
      </div>
    </div>
  </section>
</template>