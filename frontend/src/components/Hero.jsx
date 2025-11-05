'use client'

import { useState, useRef, useEffect } from 'react'
import { Dialog, DialogPanel } from '@headlessui/react'
import { Bars3Icon, XMarkIcon, ChevronDownIcon } from '@heroicons/react/24/outline'
import {
  CalendarDaysIcon,
  SparklesIcon,
  ShieldCheckIcon,
  HeartIcon,
  LifebuoyIcon,
} from '@heroicons/react/24/outline'

const services = [
  {
    name: 'Examens et Nettoyages Dentaires',
    description:
      'Prévention, dépistage des caries et nettoyage professionnel pour un sourire sain et durable.',
    icon: CalendarDaysIcon,
  },
  {
    name: 'Blanchiment et Esthétique du Sourire',
    description:
      'Traitements de blanchiment, facettes et solutions esthétiques pour raviver votre sourire.',
    icon: SparklesIcon,
  },
  {
    name: 'Soins et Restaurations Dentaires',
    description:
      'Plombages, couronnes et réparations pour restaurer confort et confiance.',
    icon: ShieldCheckIcon,
  },
  {
    name: 'Orthodontie et Alignement',
    description:
      'Appareils dentaires et gouttières invisibles pour un alignement parfait.',
    icon: HeartIcon,
  },
  {
    name: 'Chirurgie et Urgences Dentaires',
    description:
      'Extractions, implants et soins urgents assurés avec douceur et expertise.',
    icon: LifebuoyIcon,
  },
]

export default function ClinicPage() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [openIndex, setOpenIndex] = useState(null)
  const servicesRef = useRef(null)
  const bookingRef = useRef(null)

  const scrollToSection = (ref) => {
    ref.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  useEffect(() => {
    const script = document.createElement('script')
    script.src = 'https://assets.calendly.com/assets/external/widget.js'
    script.async = true
    document.body.appendChild(script)
  }, [])

  return (
    <div className="bg-white text-black relative overflow-hidden">
      

      {/* Hero Section */}
      <section className="relative isolate px-6 pt-20 lg:px-8 text-center">
        {/* Gradient background (TOP) */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        >
          <div
            className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36rem] -translate-x-1/2 rotate-[30deg] 
                       bg-gradient-to-tr from-[#2563EB] to-[#1E40AF] opacity-25 sm:left-[calc(50%-30rem)] sm:w-[72rem]"
          />
        </div>

        <div className="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
          <div className="hidden sm:mb-8 sm:flex sm:justify-center">
            <div className="relative rounded-full px-3 py-1 text-sm text-gray-700 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
              🦷 Nouvelles offres de soins disponibles.{' '}
              <a
                href="#"
                className="font-semibold text-[#2563EB] hover:text-[#1A4D9A] transition"
              >
                En savoir plus →
              </a>
            </div>
          </div>
          <h1 className="text-5xl font-semibold tracking-tight text-black sm:text-7xl">
            Votre <span className="text-[#2563EB]">Sourire,</span> Notre Priorité
          </h1>
          <p className="mt-6 text-lg text-gray-600 max-w-xl mx-auto">
            Des soins dentaires modernes et attentionnés — pensés pour votre confort et votre confiance.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row justify-center gap-4">
            <button
              onClick={() => scrollToSection(bookingRef)}
              className="rounded-md bg-[#2563EB] px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-[#1E40AF] transition"
            >
              Prendre rendez-vous
            </button>
            <button
              onClick={() => scrollToSection(servicesRef)}
              className="text-sm font-semibold text-black hover:text-[#2563EB] transition"
            >
              Voir nos services →
            </button>
          </div>
        </div>

        {/* Gradient background (BOTTOM) */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
        >
          <div
            className="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36rem] -translate-x-1/2 
                       bg-gradient-to-tr from-[#2563EB] to-[#1E40AF] opacity-25 sm:left-[calc(50%+36rem)] sm:w-[72rem]"
          />
        </div>
      </section>

      {/* Services Accordion */}
      <section ref={servicesRef} id="services" className="bg-white py-24 sm:py-32 border-t border-gray-100">
        <div className="mx-auto max-w-4xl px-6 text-center">
          <h2 className="text-sm font-semibold text-[#2563EB] uppercase tracking-wider">Pick a Service</h2>
          <p className="mt-2 text-4xl font-bold text-black sm:text-5xl">Choisissez un soin</p>

          <div className="mt-16 text-left">
            {services.map((service, index) => (
              <div key={service.name} className="border-b border-gray-200 py-4">
                <button
                  onClick={() => setOpenIndex(openIndex === index ? null : index)}
                  className="flex justify-between items-center w-full text-left"
                >
                  <div className="flex items-center gap-4">
                    <service.icon className="h-6 w-6 text-[#2563EB]" />
                    <span className="font-semibold text-lg">{service.name}</span>
                  </div>
                  <ChevronDownIcon
                    className={`h-5 w-5 text-gray-500 transition-transform duration-300 ${
                      openIndex === index ? 'rotate-180' : ''
                    }`}
                  />
                </button>
                {openIndex === index && (
                  <p className="mt-3 text-gray-600 text-base pl-10 transition-all duration-300">
                    {service.description}
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Booking (Calendly) */}
      <section ref={bookingRef} id="booking" className="py-24 bg-white text-center">
        <h3 className="text-2xl font-semibold text-[#2563EB] mb-6">Réservez votre consultation</h3>
        <div
          className="calendly-inline-widget w-full"
          data-url="https://calendly.com/mtao-pro/salem_clinique?primary_color=2563EB&text_color=000000&background_color=FFFFFF"
          style={{ minWidth: '100%', height: '100vh' }}
        ></div>
      </section>
    </div>
  )
}
