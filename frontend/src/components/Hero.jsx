export default function Hero() {
  return (
    <section
      className="relative flex items-center justify-center text-center text-[#264653] bg-cover bg-center bg-no-repeat min-h-screen"
      style={{ backgroundImage: "url('/src/assets/hero-bg.jpg')" }}
    >
      {/* Overlay (optional for better text contrast) */}
      <div className="absolute inset-0 bg-black/20"></div>

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center justify-center px-4">
        <h1 className="text-5xl sm:text-6xl font-extrabold text-white max-w-3xl leading-tight">
          Votre{" "}
          <span className="relative inline-block text-[#219EBC]">
            Sourire,
          </span>{" "}
          Notre Priorité
        </h1>

        <p className="mt-6 text-white/90 max-w-xl text-lg">
          Des soins dentaires modernes et doux, pensés pour votre confort et votre confiance.
        </p>

        <div className="mt-10 flex flex-col sm:flex-row gap-4">
          {/* Primary Button */}
          <button className="px-8 py-3 bg-[#F4A261] text-white font-semibold rounded-full hover:bg-[#F4A261]/70 hover:cursor-pointer transition-all">
            Prendre rendez-vous
          </button>

          {/* Secondary Outline Button */}
          <button className="px-8 py-3 border border-white text-white rounded-full font-medium flex items-center justify-center gap-2 hover:border-[#F4A261] hover:bg-white/10 hover:cursor-pointer transition-all">
            Voir nos services
          </button>
        </div>
      </div>
    </section>
  );
}

