import Hero from "./components/Hero";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">
            Kazakh Ornaments Identifier
          </h1>
        </div>
      </header>

      <main className="flex-grow">
        <section className="max-w-7xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
          <Hero />
        </section>
      </main>

      <footer className="bg-white shadow mt-10">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 text-center text-gray-500">
          &copy; {new Date().getFullYear()} Kazakh Ornaments Identifier. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
